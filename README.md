# 🔐 File Integrity Checker

A simple SHA256-based File Integrity Monitoring tool built with Python.

This project detects unauthorized file modifications by creating cryptographic fingerprints (SHA256 hashes) and comparing them against a saved baseline.

The goal of this project is to demonstrate core security concepts such as:

* File integrity monitoring
* Hash-based verification
* Baseline comparison
* Change detection
* Secure CLI tools
* Dockerized security applications

## ✨ Features

✅ SHA256 file hashing
✅ File integrity verification
✅ Directory scanning (recursive)
✅ Detect modified files
✅ Command-line interface (CLI)
✅ Error handling
✅ Docker support
✅ Persistent hash database using JSON

## 🛠 Technologies

* Python 3
* SHA256 Cryptographic Hashing
* JSON Database Storage
* Docker
* argparse

## 📂 Project Structure

```
file-integrity-checker/

├── main.py              # CLI application
├── hasher.py            # SHA256 hashing engine
├── database.py          # Hash storage manager
├── hashes.json          # Saved file fingerprints
├── Dockerfile           # Docker configuration
├── requirements.txt
├── important_files/     # Test directory
└── README.md
```

# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/file-integrity-checker.git
```

Enter the project directory:

```bash
cd file-integrity-checker
```

## Run with Python

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows:

```powershell
venv\Scripts\activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

# 💻 Usage

## Scan a file

Create and save the file hash:

```bash
python main.py scan test.txt
```

Example output:

```
✔ Hash saved

File: test.txt
Hash:
7505edb3842bd8dc...
```

## Check file integrity

Verify if the file was modified:

```bash
python main.py check test.txt
```

Safe result:

```
✔ File is safe
No changes detected
```

Modified file:

```
⚠ WARNING
File has been modified!

Old:
7505edb3842bd8dc...

New:
3a9caf1d7b247c97...
```

# 📁 Directory Monitoring

The tool can scan directories recursively.

Example:

```bash
python main.py scan important_files
```

Output:

```
Scanning...

✔ important_files/config.txt
✔ important_files/database.txt
✔ important_files/users.txt

3 files saved
```

Check directory:

```bash
python main.py check important_files
```

Example:

```
Checking integrity...

✔ important_files/config.txt
✔ important_files/database.txt
⚠ Modified: important_files/users.txt
```

# 🐳 Docker Usage

Build Docker image:

```bash
docker build -t file-integrity-checker .
```

Run help:

```bash
docker run --rm file-integrity-checker --help
```

Scan with Docker:

```powershell
docker run --rm `
-v ${PWD}/hashes.json:/app/hashes.json `
file-integrity-checker scan test.txt
```

Check with Docker:

```powershell
docker run --rm `
-v ${PWD}/hashes.json:/app/hashes.json `
file-integrity-checker check test.txt
```

# 🔒 Security Concepts

This project demonstrates:

* Cryptographic hashing
* SHA256 fingerprints
* Integrity verification
* Baseline security model
* File change detection

# ⚠ Disclaimer

This project is created for educational purposes to learn cybersecurity concepts and defensive security techniques.

Use it only on systems and files you own or have permission to monitor.

# 📌 Future Improvements

Planned features:

* Detect deleted files
* Detect newly created files
* Generate security reports
* Support multiple hash algorithms
* Add logging system
* Add scheduled monitoring
* Improve CLI interface

## Author

Created as a cybersecurity learning project.
