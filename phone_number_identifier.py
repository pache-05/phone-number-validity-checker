import requests

def phone_number(number):

    api_key = f"c972b3e93d1748c384c2f473cacb0b09"
    base_url = "https://phonevalidation.abstractapi.com/v1"

    params = {
        "api_key": api_key,
        "phone":number,        
        }
    
    response = requests.get(base_url, params=params)
    data = response.json()
    #print(data)
    
    if response.status_code == 200:
        details = {
            "Phone" : data["phone"],
            "valid": data["valid"],
            "international" : data["format"]["international"],
            "local": data["format"]["local"],
            "country_code" : data["country"]["code"],
            "country_name" : data["country"]["name"],
            "number_prefix" : data["country"]["prefix"],
            "location" : data["location"],
            "phone_type" : data["type"],
            "number_carrier" : data["carrier"],   
                    
        }
        if details["valid"] == False:
            print("invalid input format, try using this format e.g (2347063382277)")
        else:    
            print(f"\nvalid: {details['valid']}")
            print(f"your phone number is: {details['Phone']}")
            print(f"phone number carrier: {details['number_carrier']} Network")
            print(f"International phone number format is: {details['international']}")
            print(f"local phone number format is: {details['local']}")
            print(f"phone number country code is: {details['country_code']}")
            print(f"phone number country name is: {details['country_name']}")
            print(f"phone number prefix is: {details['number_prefix']}")
            print(f"phone number location is: {details['location']}")
            print(f"phone type: {details['phone_type']}")
            return
           
    else:
        print("Server Error")
        
try:
    def phone():
        numbers =int(input("Type your phone number (e.g 23412345678): ").strip())
        print(phone_number(numbers))

    phone()

except ValueError:
    print(f"Do not include space in your number (e.g 234 1 2345678) ❌\ninstead use 2347063382277 ✅")

except requests.exceptions.Timeout:
    print("invalid input format, try using this format e.g (2347063382277)")

except requests.exceptions.ConnectionError:
    print("Check your internet connection")
