import requests
import time
import os

ENV_FILE = ".env"

def load_from_env_file(key):
    """Carica chiave da file .env manualmente."""
    if not os.path.exists(ENV_FILE):
        return None

    try:
        with open(ENV_FILE, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    env_key, value = line.split('=', 1)
                    if env_key.strip() == key:
                        return value.strip()
    except:
        pass
    return None

def save_to_env_file(key, value):
    """Salva chiave in .env (sovrascrive se esiste)."""
    try:
        key_line = f"{key}={value}\n"
        if os.path.exists(ENV_FILE):
            with open(ENV_FILE, 'r') as f:
                lines = f.readlines()
            # Sostituisci riga esistente o aggiungi
            found = False
            for i, line in enumerate(lines):
                if line.strip().startswith(f"{key}="):
                    lines[i] = key_line
                    found = True
                    break
            if not found:
                lines.append(key_line)
        else:
            lines = [key_line]

        with open(ENV_FILE, 'w') as f:
            f.writelines(lines)
        print(f"✅ API key saved to {ENV_FILE}")
    except Exception as e:
        print(f"❌ Error saving .env: {e}")

def get_api_config():
    """Load API key from .env file, environment, or prompt user."""
    api_key = os.getenv("NVD_API_KEY") or load_from_env_file("NVD_API_KEY")

    if not api_key:
        print("\n[!] NVD_API_KEY not found in environment or .env file.")
        api_key = input("Enter your API Key (or press Enter to proceed limited): ").strip()

        if api_key:
            save_to_env_file("NVD_API_KEY", api_key)
            os.environ["NVD_API_KEY"] = api_key  # Per sessione corrente
        else:
            print("Proceeding in limited mode (no API key - slower rate limits).")

    return api_key

def search_vendor_by_keyword(keyword):
    """Search database for vendors matching a keyword."""
    api_key = get_api_config()
    url = "https://services.nvd.nist.gov/rest/json/cpes/2.0"
    params = {
        "keywordSearch": keyword,
        "resultsPerPage": 100  # Enough sample to identify vendors
    }
    headers = {"apiKey": api_key} if api_key else {}

    print(f"Searching vendors for '{keyword}'...")
    try:
        response = requests.get(url, headers=headers, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        vendors = set()
        for item in data.get("products", []):
            cpe_name = item['cpe']['cpeName']
            parts = cpe_name.split(':')
            if len(parts) > 3:
                vendors.add(parts[3])  # Vendor is 4th position in CPE 2.3

        return sorted(list(vendors))
    except Exception as e:
        print(f"Error during vendor search: {e}")
        return []

def fetch_products(vendor, part="*"):
    """Fetch all products for a specific vendor (optimized pagination)."""
    api_key = get_api_config()
    url = "https://services.nvd.nist.gov/rest/json/cpes/2.0"
    params = {
        "cpeMatchString": f"cpe:2.3:{part}:{vendor}:*:*:*:*:*:*:*",
        "resultsPerPage": 1000,
        "startIndex": 0
    }
    headers = {"apiKey": api_key} if api_key else {}
    all_products = set()

    print(f"Fetching products for vendor '{vendor}' (category: {part})...")

    while True:
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            if response.status_code == 403:
                print("Rate limit hit! Waiting 30s...")
                time.sleep(30)
                continue

            response.raise_for_status()
            data = response.json()

            for item in data.get("products", []):
                p = item['cpe']['cpeName'].split(':')
                if len(p) > 4:
                    all_products.add(p[4])

            total = data.get("totalResults", 0)
            fetched = params["startIndex"] + len(data.get("products", []))
            print(f"Progress: {fetched}/{total} products")

            if fetched >= total:
                break
            params["startIndex"] += params["resultsPerPage"]
            time.sleep(6 if api_key else 30)

        except Exception as e:
            print(f"Error fetching products: {e}")
            break

    return sorted(list(all_products))

def main():
    print("🚀 NIST NVD CPE Extractor - Zero Dependencies Version")
    while True:
        print("\n" + "="*50)
        print("1. 🔍 Search Vendor names (by keyword)")
        print("2. 📦 Extract all products for a Vendor")
        print("3. ❌ Exit")
        print("="*50)

        choice = input("Select an option [1-3]: ").strip()

        if choice == "1":
            keyword = input("\nEnter keyword (e.g. 'forti', 'cisco', 'apache'): ").strip()
            if not keyword:
                print("❌ Empty keyword. Try again.")
                continue

            results = search_vendor_by_keyword(keyword)
            if results:
                print(f"\n✅ {len(results)} vendors found:")
                for i, vendor in enumerate(results, 1):
                    print(f"  {i:2d}. {vendor}")
            else:
                print("❌ No vendors found for this keyword.")

        elif choice == "2":
            vendor = input("\nEnter exact vendor name (lowercase): ").strip().lower()
            if not vendor:
                print("❌ Empty vendor name. Try again.")
                continue

            category = input("Category [a=app, o=os, h=hw, *=all] (default *): ").strip() or "*"
            products = fetch_products(vendor, category)

            print(f"\n✅ Total products found: {len(products)}")
            if products:
                print("\n📋 Products list:")
                # Lista puntata verticale per TUTTI i prodotti
                for i, product in enumerate(products, 1):
                    print(f"  • {product}")
                
                # Opzione per mostrare solo primi 10 se sono tanti
                if len(products) > 10:
                    print(f"\n   ... e altri {len(products) - 10} prodotti")

                save_choice = input("\n💾 Save to TXT file? (y/n): ").strip().lower()
                if save_choice == 'y':
                    filename = f"{vendor}_{category}_products.txt"
                    with open(filename, "w") as f:
                        f.write(f"# NIST CPE Products for {vendor} ({category})\n")
                        f.write(f"# Total: {len(products)}\n")
                        f.write("\n".join(products))
                    print(f"✅ Saved to {filename}")
            else:
                print("❌ No products found.")

        elif choice == "3":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

