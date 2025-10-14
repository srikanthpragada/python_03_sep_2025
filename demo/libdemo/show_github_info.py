import requests

resp = requests.get("https://api.github.com/users/gvanrossum")

if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

details = resp.json()

print(f"Name    : {details['name']}")
print(f"Company : {details['company']}")
print(f"Location: {details['location']}")


