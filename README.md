# raju-s-pythonkeylogger

raju-s-keylogger
A simple Python keylogger that logs all keyboard activity to a file called log.txt. Supports both regular character keys and special keys (Space, Enter, Shift, etc.) with cross-platform compatibility.

Features
Captures every key press including special keys.

Logs all activity to log.txt in real-time.

Uses the robust pynput library for keyboard event capture.

Requirements
Python 3.x

pynput library

Install requirements with:

bash
pip install pynput
How to Download and Run on Kali Linux
1. Download the Script
If hosted on GitHub, use:

bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Or, download the file directly:

bash
wget https://github.com/yourusername/your-repo-name/raw/main/raju-s-keylogger.py
2. Install Python and Dependencies
Ensure Python and pip are installed:

bash
sudo apt update
sudo apt install python3 python3-pip
pip3 install pynput
For the modern Kali setup (recommended isolation):

bash
sudo apt install pipx
pipx install pynput
3. Run the Script
Start the keylogger on Kali Linux with:

bash
python3 raju-s-keylogger.py
Keypresses will be logged to log.txt in the same directory. Stop with Ctrl + C.

Code Explanation
Uses pynput.keyboard.Listener to detect keypresses.

Logs normal characters with key.char; logs special keys with their names.

Script continues recording until terminated.

Disclaimer
This tool is for ethical, educational, and authorized testing only. Always obtain proper permission before using keyloggers.
