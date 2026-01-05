# Mini SQL Injection Scanner 🛡️

This project is a simple Python-based SQL Injection scanner created
for educational purposes and local lab testing such as DVWA.

## Features
- Tests basic SQL Injection payloads
- Detects SQL error messages
- Easy to understand for beginners

## Requirements
- Python 3
- requests library

## Usage
Example using DVWA SQL Injection module:
python scanner.py

Input:
Target URL: http://localhost/DVWA/vulnerabilities/sqli/
Parameter: id

Install dependencies:
```bash
pip install requests
