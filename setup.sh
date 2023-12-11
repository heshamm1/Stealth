#!/bin/bash

echo -e "\033[91m"
echo ' _______  _______  _______  _______  ___      _______  __   __   '
echo '|       ||       ||       ||   _   ||   |    |       ||  | |  |  '
echo '|  _____||_     _||    ___||  |_|  ||   |    |_     _||  |_|  |  '
echo '| |_____   |   |  |   |___ |       ||   |      |   |  |       |  '
echo '|_____  |  |   |  |    ___||       ||   |___   |   |  |       |  '
echo ' _____| |  |   |  |   |___ |   _   ||       |  |   |  |   _   |  '
echo '|_______|  |___|  |_______||__| |__||_______|  |___|  |__| |__|  '
echo '               The Way to gain an XSS from PDF                     '
echo '                     Created By @heshamm1\033[0m'

echo -e "\nInstalling dependencies..."
pip install -r requirements.txt

echo -e "\nSetup complete! You can now run the tool using the following command:"
echo -e "\n\033[91mpython stealth.py\033[0m"
