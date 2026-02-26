NIST NVD CPE Extractor 🛡️<br>
<br>
Extract Vendors and Products from NIST NVD CPE Database - Zero configuration, auto-saves API key.<br>
<br>
✨ Quick Demo<br>
python nvd_cpe_extractor.py
<br>
1. Enter API key once → auto-saves to .env
2. Search "fortinet" → lists exact vendors  
3. Extract "fortinet" → 5000+ products → saves TXT

🚀 Linux Installation (5 seconds)<br>
Automatic Installer<br>
<br>
chmod +x install_deps.sh<br>
./install_deps.sh<br>
source nvd_env/bin/activate<br>
python nvd_cpe_extractor.py<br>
<br>
Manual (Ubuntu/Debian)<br>
<br>
sudo apt update<br>
sudo apt install -y python3 python3-pip python3-venv<br>
python3 -m venv nvd_env<br>
source nvd_env/bin/activate<br>
pip install requests<br>
python nvd_cpe_extractor.py<br>
🔑 NIST NVD API Key (Free)<br>
Register: https://nvd.nist.gov/developers/request-an-api-key<br>

Fill form:<br>
<br>
Name: Name Surname<br>
Email: your.email@company.it<br>
Organization: Your Company<br>
Phone: + ...<br>
Verify email → Key in 1-2 days<br>

Format: abc123def456ghi789jkl012mno345pqr

First run → prompts key → auto-saves to .env
Future runs → loads automatically ✅

📊 Rate Limits Comparison<br>
Mode	Requests/30s	Requests/min<br>
No key	5	50<br>
With key	50	1,000<br>
<br>
📖 Usage Examples<br>
<br>
🚀 NIST NVD CPE Extractor<br>
<br>
1. 🔍 Search Vendor names (by keyword)<br>
2. 📦 Extract all products for a Vendor  <br>
3. ❌ Exit<br>
<br>
Example 1: Find Vendors<br>
<br>
Enter keyword: forti<br>
✅ 12 vendors found:<br>
   1. fortinet<br>
   2. fortianalyzer<br>
   3. fortiweb<br>
<br>
Example 2: Extract Products<br>
<br>
Enter vendor: fortinet<br>
Category: *<br>
Fetching products... Progress: 2500/5432<br>
✅ Total products: 5432<br>
💾 Save to TXT? (y/n): y<br>
✅ Saved to fortinet_*_products.txt<br>
<br>
📁 Repository Structure<br>
<br>
nvd_cpe_extractor/<br>

| File                          | Descrizione              |
|-------------------------------|--------------------------|
| `nvd_cpe_extractor.py`        | # Main script            |
| `README.md`                   | # This file              |
| `install_deps.sh`             | # Linux installer        |
| `requirements.txt`            | # Python deps            |
| `.env.example`                | # API key template       |
| `.gitignore`                  | # Excludes .env          |
| `fortinet_products.txt`       | # Example output         |


🛡️ Features<br>
<br>
✅ Zero external dependencies (uses requests)<br>
✅ Auto-saves API key to .env (git-ignored)<br>
✅ Intelligent rate limiting (6s with key, 30s without)<br>
✅ Full CPE 2.3 support<br>
✅ Category filtering (app/os/hw/all)<br>
<br>
🎯 Perfect For<br>
<br>
✅ SIEM/SOAR integrations<br>
✅ Vulnerability scanners<br>
✅ Asset inventory<br>
✅ Compliance reporting<br>
✅ Cybersecurity research<br>
✅ Red/Blue team recon<br>
🐳 Docker (Optional)<br>
<br><br>
FROM python:3.11-slim <br>
WORKDIR /app <br>
COPY . . <br>
RUN pip install requests <br>
CMD ["python", "nvd_cpe_extractor.py"] <br>


docker build -t nvd-extractor . <br>
docker run -it -v $(pwd):/app nvd-extractor <br>
<br>
🛠️ Troubleshooting<br>
Issue	Solution<br>
403 Rate Limit	Auto-retries after 30s <br>
Timeout	Network issue, retry <br>
.env permissions	chmod 600 .env <br><br>
No products found	Try exact vendor name from option 1
<br>
🤝 Contributing <br>
Fork repository<br>

Test with known vendors (cisco, fortinet, apache)

PR improvements

⭐ if useful!

📄 License<br>
MIT License - Free for personal/commercial use.<br>
<br>
Made for IT Infrastructure & Cybersecurity Pros<br>
Mauro Longhi | Seriate, Lombardia, Italy<br>
Linux - Proxmox - DevOps - Networking<br>
February 2026<br>

# Quick start alias<br>
alias nvd="source nvd_env/bin/activate && python nvd_cpe_extractor.py"

