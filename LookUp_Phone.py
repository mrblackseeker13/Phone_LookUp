import phonenumbers
import requests

def reverse_phone_lookup(number):
    url = f'http://apilayer.net/api/validate?access_key=YOUR_ACCESS_KEY&number={Po6QXIu1xBKBguQJ8uv4xj7Cf8ZwcfiQ}&country_code=IN&format=1'
    response = requests.get(url)
    data = response.json()
    if data['valid']:
        parsed_number = phonenumbers.parse(number, "IN")
        print(f"Phone number: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        print(f"Location: {phonenumbers.region_name_for_number(parsed_number, 'en')}")
        print(f"Carrier: {data['carrier']}")
        print(f"Line type: {data['line_type']}")
    else:
        print("Invalid phone number")

# Example usage
reverse_phone_lookup('+919876543210')
