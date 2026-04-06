import requests
import json
import os

# QRadar Məlumatları
QRADAR_IP = "13.62.57.185" # Sənin QRadar IP-n
API_TOKEN = "9aba895b-9bee-47f4-9e63-e9b99f8ddc58"
HEADERS = {
    'SEC': API_TOKEN,
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

def deploy_rule(file_path):
    with open(file_path, 'r') as f:
        rule_data = json.load(f)
    
    # QRadar API Endpoint (Rules yaratmaq üçün)
    url = f"https://{QRADAR_IP}/api/analytics/rules"
    
    response = requests.post(url, headers=HEADERS, json=rule_data, verify=False)
    
    if response.status_code == 201:
        print(f"Uğurlu: {rule_data['name']} QRadar-a göndərildi.")
    else:
        print(f"Xəta: {response.status_code} - {response.text}")

# Qovluqdakı bütün JSON-ları göndər
rules_folder = "qradar_rules/"
for filename in os.listdir(rules_folder):
    if filename.endswith(".json"):
        deploy_rule(os.path.join(rules_folder, filename))
