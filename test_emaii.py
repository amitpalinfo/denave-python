import requests

url = 'http://localhost:5000/send-email'
data = {'recipient': 'amitmahto64@gmail.com'}
response = requests.post(url, json=data)

print("ss",response.json())
