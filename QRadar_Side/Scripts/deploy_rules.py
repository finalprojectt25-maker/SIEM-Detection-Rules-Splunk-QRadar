import requests
import json

# Connection Details
QRADAR_IP = "13.50.16.252"
API_TOKEN = "9aba895b-9bee-47f4-9e63-e9b99f8ddc58" # Bura bayaq aldigin tokeni qoyacaqsan

def deploy_rules_to_siem():
    print(f"Connecting to QRadar at {QRADAR_IP}...")
    
    # Header configuration for API
    headers = {
        'SEC': API_TOKEN,
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    # In a professional scenario, this script reads files from the /Detection_Rules folder
    # and sends them to QRadar's REST API endpoint.
    
    # Example logic:
    # response = requests.get(f"https://{QRADAR_IP}/api/analytics/rules", headers=headers, verify=False)
    # print("Rules successfully synced from GitHub!")

if __name__ == "__main__":
    deploy_rules_to_siem()
