import requests

url = "https://api.openaq.org/v2/countries"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)