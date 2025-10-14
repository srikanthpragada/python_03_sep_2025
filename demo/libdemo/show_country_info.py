import requests

code = input("Enter country code :")
resp = requests.get(f"https://restcountries.com/v3.1/alpha/{code}")

if resp.status_code != 200:
    print('Sorry! Could not get details!')
    exit()

countries = resp.json()
country = countries[0]

print(f"Name          : {country['name']['common']}")
print(f"Capital       : {country['capital'][0]}")
print(f"Area(KM)      : {country['area']}")
print(f"Population(m) : {country['population'] // (1000000)}")


