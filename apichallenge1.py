import requests
import json

url = 'http://challenge.code2040.org/api/register'
dictionary = {'token': '5704643fa526b42f42e46f97740539a4', 'github' : 'https://github.com/itstemo/Code2040'}

r = requests.post(url, data=dictionary)

r.text
r.status_code

