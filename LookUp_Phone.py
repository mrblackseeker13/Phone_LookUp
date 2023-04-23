import requests
def numverify_lookup(phone_number, api_key):
    base_url = "http://apilayer.net/api/validate"
    params = {
        "access_key": api_key,
        "number": phone_number,
        "format": 1
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error: {response.status_code}")
if __name__ == "__main__":
    api_key = "YOUR_API_KEY"
    phone_number = input("Enter a phone number to validate: ")
    try:
        result = numverify_lookup(phone_number, api_key)
        print(f"Validation Result: {result}")
    except Exception as e:
        print(e)
