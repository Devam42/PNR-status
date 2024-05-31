import requests
import json


pnr_numbers = [
    "2758593543", "2761981310", "6134979034", "2758593543", "4910024233",
    "4164403703", "4200665257", "2313446108", "6134863748", "4820522864",
    "2861910669", "6534551448", "6235931548", "6735889710", "6536038402"
]


#url = 'https://pnr-status.onrender.com/api/pnr-status'  
url = 'http://192.168.18.137:5000/'

def is_camel_case(s):
    return s != s.lower() and s != s.upper() and "_" not in s

def check_camel_case_keys(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if not is_camel_case(key):
                return False
            if isinstance(value, (dict, list)):
                if not check_camel_case_keys(value):
                    return False
    elif isinstance(data, list):
        for item in data:
            if not check_camel_case_keys(item):
                return False
    return True

# Test the PNR numbers
for pnr in pnr_numbers:
    response = requests.post(url, json={'pnr': pnr})
    if response.status_code == 200:
        response_data = response.json()
        print(f"PNR: {pnr}")
        print("Response JSON:")
        print(json.dumps(response_data, indent=4))
        
        # Check if the response keys are in camelCase
        if check_camel_case_keys(response_data):
            print("All keys are in camelCase.")
        else:
            print("Some keys are not in camelCase.")
    else:
        print(f"Failed to fetch PNR status for {pnr}. HTTP Status Code: {response.status_code}")
        print(response.text)
    print()




