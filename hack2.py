# Import requests module to send HTTP requests
import requests

# Define the phone number to get the IP address from
phone_number = '+919876543210'

# Define the headers for the Truecaller request
# You need to provide your own API key and app name
headers = {
    'X-Truecaller-Key': 'your_api_key_here',
    'X-Truecaller-AppName': 'your_app_name_here',
}

# Define the parameters for the Truecaller request
params = {
    'phoneNumber': phone_number,
}

# Send the Truecaller request and get the response
response = requests.get('https://api4.truecaller.com/v1/phone', headers=headers, params=params)
print(response.status_code)
print(response.json())

# Extract the country and city of the phone number from the response
# You may need to handle errors or missing data
country = response.json().get('country')
city = response.json().get('city')

# Define the parameters for the ipapi request
# You need to provide your own API key
params = {
    'access_key': 'your_api_key_here',
    'country': country,
    'city': city,
}

# Send the ipapi request and get the response
response = requests.get('https://api.ipapi.com/api/check', params=params)
print(response.status_code)
print(response.json())

# Extract the list of IP addresses from the response
# You may need to handle errors or missing data
ip_list = response.json().get('ip_list')

# Print the list of IP addresses
print('The possible IP addresses for the phone number are:')
for ip in ip_list:
    print(ip)
