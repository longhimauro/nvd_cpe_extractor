NIST NVD CPE Extractor 🛡️

Extract Vendors and Products from NIST NVD CPE Database - Zero configuration, auto-saves API key.

✨ Quick Demo

python nvd_cpe_extractor.py

# 1. Enter API key once → auto-saves to .env
# 2. Search "fortinet" → lists exact vendors  
# 3. Extract "fortinet" → 5000+ products → saves TXT

🚀 Linux Installation (5 seconds)
Automatic Installer

chmod +x install_deps.sh
./install_deps.sh
source nvd_env/bin/activate
python nvd_cpe_extractor.py

Manual (Ubuntu/Debian)

sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 -m venv nvd_env
source nvd_env/bin/activate
pip install requests
python nvd_cpe_extractor.py
🔑 NIST NVD API Key (Free)
Register: https://nvd.nist.gov/developers/request-an-api-key

Fill form:

Name: Name Surname
Email: your.email@company.it
Organization: Your Company
Phone: + ...
Verify email → Key in 1-2 days

Format: abc123def456ghi789jkl012mno345pqr

First run → prompts key → auto-saves to .env
Future runs → loads automatically ✅

📊 Rate Limits Comparison
Mode	Requests/30s	Requests/min
No key	5	50
With key	50	1,000

📖 Usage Examples

🚀 NIST NVD CPE Extractor
==================================================
1. 🔍 Search Vendor names (by keyword)
2. 📦 Extract all products for a Vendor  
3. ❌ Exit
==================================================

Example 1: Find Vendors

Enter keyword: forti
✅ 12 vendors found:
   1. fortinet
   2. fortianalyzer
   3. fortiweb

Example 2: Extract Products

Enter vendor: fortinet
Category: *
Fetching products... Progress: 2500/5432
✅ Total products: 5432
💾 Save to TXT? (y/n): y
✅ Saved to fortinet_*_products.txt

📁 Repository Structure

nvd_cpe_extractor/
├── nvd_cpe_extractor.py     # Main script
├── README.md               # This file
├── install_deps.sh         # Linux installer
├── requirements.txt        # Python deps
├── .env.example           # API key template
├── .gitignore             # Excludes .env
└── fortinet_products.txt  # Example output

🛡️ Features
✅ Zero external dependencies (uses requests)

✅ Auto-saves API key to .env (git-ignored)

✅ Intelligent rate limiting (6s with key, 30s without)

✅ Full CPE 2.3 support

✅ Category filtering (app/os/hw/all)

🎯 Perfect For

✅ SIEM/SOAR integrations
✅ Vulnerability scanners
✅ Asset inventory
✅ Compliance reporting
✅ Cybersecurity research
✅ Red/Blue team recon
🐳 Docker (Optional)


FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install requests
CMD ["python", "nvd_cpe_extractor.py"]


docker build -t nvd-extractor .
docker run -it -v $(pwd):/app nvd-extractor
🛠️ Troubleshooting
Issue	Solution
403 Rate Limit	Auto-retries after 30s
Timeout	Network issue, retry
.env permissions	chmod 600 .env
No products found	Try exact vendor name from option 1
🤝 Contributing
Fork repository

Test with known vendors (cisco, fortinet, apache)

PR improvements

⭐ if useful!

📄 License
MIT License - Free for personal/commercial use.

Made for IT Infrastructure & Cybersecurity Pros
Mauro Longhi | Seriate, Lombardia, Italy
Linux - Proxmox - DevOps - Networking
February 2026

# Quick start alias
alias nvd="source nvd_env/bin/activate && python nvd_cpe_extractor.py"

