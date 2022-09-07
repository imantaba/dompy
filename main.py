import requests


url = "https://api.openaq.org/v2/sources?limit=100&page=1&offset=0&sort=asc&order_by=sourceName"


headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers)
print(response.text)