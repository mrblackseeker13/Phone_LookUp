import requests

# Replace YOUR_API_KEY with your actual API key
api_key = "YOUR_API_KEY"

# Replace PHONE_NUMBER with the phone number you want to lookup
phone_number = "PHONE_NUMBER"

# Make an HTTP GET request to the API endpoint
response = requests.get(f"https://apilayer.net/api/validate?access_key={Po6QXIu1xBKBguQJ8uv4xj7Cf8ZwcfiQ}&number={phone_number}&country_code=IN&format=1")

# Parse the JSON response
data = response.json()

# Print the information about the phone number
if data["valid"]:
    print(f"Phone number: {data['number']}")
    print(f"Country: {data['country_name']} ({data['country_code']})")
    print(f"Location: {data['location']}")
    print(f"Carrier: {data['carrier']}")
    print(f"Line type: {data['line_type']}")
else:
    print("Invalid phone number")
