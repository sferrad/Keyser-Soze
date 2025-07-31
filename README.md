# 🧪 Keyser Soze (Python Keylogger — Educational Version)

   ## ⚠️ DISCLAIMER:
  This software is intended for educational and testing purposes only.
   Do not use it to monitor or collect data from devices or users without explicit consent.
  Unauthorized use of surveillance software is illegal and may result in criminal charges.


## 📚 Description

This project is a simple Python-based keylogger, created as part of a security learning experiment.
It demonstrates how to use the pynput library to log:

  - Keyboard input

-  Mouse clicks <br>

The program writes the captured data to a local file for analysis.<br>
## ✅ Features

  - Logs all keyboard activity

  - Logs mouse clicks with coordinates

  - Saves everything to a .txt file

  - Minimal console output (optionally silent if compiled to .exe)

## 🧰 Requirements

   - Python 3.6+

   - pynput library

## To install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

  - Clone the repository
```bash
git clone git@github.com:sferrad/Keyser-Soze.git
cd Keyser-Soze
```
- (Optional) Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate       # On Linux/macOS
venv\Scripts\activate.bat      # On Windows
```
- Install the dependencies
```bash
pip install -r requirements.txt
```
- Run the script
```bash
python3 keyser-soze.py
```
- All logs are saved in:
```
key-soze.txt
```
## 💻 Compile to Windows Executable (Optional)

To generate a .exe file:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole keyser-soze.py
```
The resulting .exe will be located in the dist/ folder.<br>
## ❌ Do NOT Use For

  - Monitoring someone else's computer without their knowledge

 - Capturing credentials or private data

- Deploying on machines you do not own or control



⚠️ **Any of the above uses are unethical and illegal under most jurisdictions.**
