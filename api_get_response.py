import requests

url = "https://api.openaq.org/v2/countries/country_id?limit=200&page=1&offset=0&sort=asc&order_by=country"

headers = {"Accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)