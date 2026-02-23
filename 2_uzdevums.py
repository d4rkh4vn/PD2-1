nodes = [
    {"hostname": "Srv-Web-01", "ip": "10.0.1.1", "status": "UP", "latency": 120},
    {"hostname": "Srv-DB-02", "ip": "10.0.1.2", "status": "UP", "latency": 80},
    {"hostname": "Srv-Mail-03", "ip": "10.0.2.1", "status": "UP", "latency": 150},
    {"hostname": "Srv-File-04", "ip": "192.168.1.10", "status": "UP", "latency": 45},
    {"hostname": "Workstation-A", "ip": "192.168.1.20", "status": "DOWN", "latency": 0},
    {"hostname": "Workstation-B", "ip": "192.168.1.21", "status": "UP", "latency": 105},
    {"hostname": "Router-Core", "ip": "192.168.0.1", "status": "UP", "latency": 90},
    {"hostname": "Router-Edge", "ip": "192.168.0.2", "status": "DOWN", "latency": 0},
    {"hostname": "Srv-Backup-05", "ip": "192.168.2.5", "status": "UP", "latency": 200},
    {"hostname": "Srv-Test-06", "ip": "192.168.2.6", "status": "UP", "latency": 95}
]

up_servers = [node for node in nodes if node["status"].upper() == "UP"]
print(f"Kopā UP serveru: {len(up_servers)}")
print("UP serveru nosaukumi:")
for node in up_servers:
    print(node["hostname"]) 
