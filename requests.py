import requests

URL = 'http://192.168.0.53'
r = requests.options(URL)
print(r.text)
