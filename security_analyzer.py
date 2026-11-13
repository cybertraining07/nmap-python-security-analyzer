import pandas as pd

# Load security scan results
df = pd.read_csv("security_scan.csv")

# Calculate statistics
total = len(df)
opened = len(df[df["Status"] == "Open"])
closed = len(df[df["Status"] == "Closed"])

# Identify potentially risky services
risky_services = ["FTP", "Telnet"]

risks = df[
    (df["Status"].str.upper() == "OPEN") &
    (df["Service"].str.upper().isin(risky_services))
]

# Display report
print("\n===== SECURITY SCAN REPORT =====")
print("Total records:", total)
print("Open ports:", opened)
print("Closed ports:", closed)

print("\n===== SERVICE ANALYSIS =====")
print(df["Service"].value_counts())

print("\n===== POTENTIALLY RISKY OPEN SERVICES =====")

if not risks.empty:
    print(risks)
else:
    print("No potentially risky open services detected.")

print("\n===== OPEN PORTS =====")
print(df[df["Status"].str.upper() == "OPEN"])

print("\n================================")

# Generate CSV security reports

summary = pd.DataFrame({
    "Metric": [
        "Total Records",
        "Open Ports",
        "Closed Ports",
        "Potentially Risky Open Services"
    ],
    "Value": [
        total,
        opened,
        closed,
        len(risks)
    ]
})

summary.to_csv("security_report.csv", index=False)

risks.to_csv("risky_services.csv", index=False)

print("\nSecurity reports saved successfully!")
print("- security_report.csv")
print("- risky_services.csv")
