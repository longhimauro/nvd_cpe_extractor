#!/bin/bash
echo "🚀 NIST CPE Extractor - Linux Installer"
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 -m venv nvd_env
source nvd_env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Installazione completata!"
echo "source nvd_env/bin/activate && python nvd_cpe_extractor.py"
