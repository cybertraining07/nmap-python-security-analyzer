# Nmap Network Scanning and Python Security Analysis

## Project Overview
A hands-on cybersecurity portfolio project demonstrating local network scanning, automated Nmap XML parsing, port analysis, and CSV report generation using Python and Pandas.

## Project Objectives
- Identify open network ports and running services.
- Perform local network scanning with Nmap.
- Parse Nmap XML output using Python.
- Analyze scan results using Pandas.
- Generate structured CSV security reports.
- Document findings and security recommendations.

## Technologies Used
- Kali Linux
- Python 3.12
- Nmap 7.94SVN
- Pandas
- XML ElementTree
- CSV

## Scan Results

| Port | Protocol | State | Detected Service |
|---|---|---|---|
| 8000 | TCP | Open | Splunkd httpd |
| 8089 | TCP | Open | Splunkd httpd |

- Open ports: 2
- Aggregated closed ports: 998

## Project Structure

```text
.
├── nmap_analyzer.py
├── nmap_scan.xml
├── nmap_results.csv
├── security_analyzer.py
├── security_scan.csv
├── security_report.csv
├── risky_services.csv
├── security_findings.md
└── README.md
```

## How to Run

### 1. Activate the virtual environment

```bash
source venv/bin/activate
```

### 2. Run the Nmap scan

```bash
nmap -sV -oX nmap_scan.xml 127.0.0.1
```

### 3. Run the Python analyzer

```bash
python nmap_analyzer.py
```

### 4. Review the CSV report

```bash
cat nmap_results.csv
```

## Key Skills Demonstrated
- Network reconnaissance
- Port and service identification
- Python scripting
- XML parsing
- Data analysis with Pandas
- Automated report generation
- Basic security findings documentation

## Scope and Ethics
This project was conducted against localhost (127.0.0.1) in a controlled lab environment. Scanning was limited to a system under my control.

The detected services are observations, not confirmed vulnerabilities.

## Author
Cybersecurity Portfolio Project
