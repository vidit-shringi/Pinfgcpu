# Import requests module to send HTTP requests
import requests

# Define the server token and device token for Firebase Cloud Messaging (FCM)
serverToken = 'your_server_token_here'
deviceToken = 'your_device_token_here'

# Define the headers for the FCM request
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + serverToken,
}

# Define the body for the FCM request
# You can customize the notification title, body, and type
# You can also add data payload if needed
body = {
    'notification': {
        'title': 'Hello from Copilot',
        'body': 'This is a test notification',
        'type': 'info', # info, error, warning or success
    },
    'to': deviceToken,
    'priority': 'high',
}

# Send the FCM request and get the response
response = requests.post('https://fcm.googleapis.com/fcm/send', headers=headers, json=body)
print(response.status_code)
print(response.json())

# Define a callback function to handle the notification click event
# This function will get the IP address of the device and print it
def on_notification_click():
    # Import socket module to get the IP address
    import socket
    # Get the hostname of the device
    hostname = socket.gethostname()
    # Get the IP address of the device
    ip_address = socket.gethostbyname(hostname)
    # Print the IP address
    print('Your IP address is:', ip_address)

# Register the callback function to the FCM service
# You may need to use a different method depending on your FCM client library
fcm.register_callback(on_notification_click)
