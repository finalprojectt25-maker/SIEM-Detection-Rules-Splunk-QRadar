import requests
import json
import urllib3

# Sertifikat xətalarını gizlətmək üçün
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def deploy_rule(rule_data):
    url = "https://<QRADAR_IP>/api/analytics/rules"
    headers = {
        'SEC': 'YOUR_API_TOKEN',
        'Content-Type': 'application/json',
        'Version': '15.0' # QRadar versiyana uyğun olaraq dəyiş
    }
    
    # QRadar-da qayda yaradarkən "content" sahəsi mütləq düzgün formatda olmalıdır
    response = requests.post(url, headers=headers, data=json.dumps(rule_data), verify=False)
    
    if response.status_code == 201:
        print("Qayda uğurla əlavə edildi!")
    else:
        print(f"Xəta baş verdi: {response.status_code}, {response.text}")
