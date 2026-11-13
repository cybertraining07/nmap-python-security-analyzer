import xml.etree.ElementTree as ET
import pandas as pd

# Load Nmap XML file
tree = ET.parse("nmap_scan.xml")
root = tree.getroot()

results = []

# Extract host and port information
for host in root.findall("host"):

    address = host.find("address")

    if address is None:
        continue

    ip = address.get("addr")

    ports = host.find("ports")

    if ports is None:
        continue

    for port in ports.findall("port"):

        state_element = port.find("state")
        service = port.find("service")

        state = state_element.get("state") if state_element is not None else "unknown"

        results.append({
            "IP": ip,
            "Protocol": port.get("protocol"),
            "Port": int(port.get("portid")),
            "State": state,
            "Service": service.get("name") if service is not None else "unknown",
            "Product": service.get("product", "unknown") if service is not None else "unknown",
            "Version": service.get("version", "unknown") if service is not None else "unknown",
            "Tunnel": service.get("tunnel", "none") if service is not None else "none"
        })

# Convert results into Pandas DataFrame
df = pd.DataFrame(results)

print("\n===== NMAP SECURITY ANALYSIS =====")
print(df.to_string(index=False))

# Calculate statistics
if not df.empty:
    open_ports = len(df[df["State"] == "open"])
    closed_ports = len(df[df["State"] == "closed"])

    # Count aggregated ports reported by Nmap
    aggregate_closed = 0

    for host in root.findall("host"):
        ports_element = host.find("ports")

        if ports_element is not None:
            for extra in ports_element.findall("extraports"):
                if extra.get("state") == "closed":
                    aggregate_closed += int(extra.get("count", 0))

    print("\n===== SCAN SUMMARY =====")
    print("Individually listed ports:", len(df))
    print("Open ports:", open_ports)
    print("Individually listed closed ports:", closed_ports)
    print("Additional aggregated closed ports:", aggregate_closed)
    print("Total closed ports:", closed_ports + aggregate_closed)

    df.to_csv("nmap_results.csv", index=False)
    print("\nReport saved: nmap_results.csv")

else:
    print("No individual port records found in XML.")
