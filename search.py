import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "terms": "cafe",
    "location": "OC"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
for business in businesses:
    business["name"]

names = [business["name"]
         for business in businesses if business["rating"] > 0]
print(names)
