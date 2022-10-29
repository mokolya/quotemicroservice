# Author: Olga Mokshantseva
# Date: 10/27/2022
# Description:
import requests

url = r'http://127.0.0.1:5000'
# GET Only
r = requests.get(url)
# URL, Response
print("Request HTTP GET "+r.url)
print("Received HTTP GET response "+ r.text)

