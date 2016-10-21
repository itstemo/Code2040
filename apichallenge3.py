import requests

url ='http://challenge.code2040.org/api/haystack'
tokenDictionary = {'token' : '5704643fa526b42f42e46f97740539a4'}

r = requests.post(url, data=tokenDictionary)

print(r.text);

dictionary = r.json()

needle = dictionary['needle']
haystack = dictionary['haystack']

print(needle)
print(haystack)

needleIndex = haystack.index(needle);

validateURL = 'http://challenge.code2040.org/api/haystack/validate'

validateDict = {'token': '5704643fa526b42f42e46f97740539a4', 'needle': needleIndex}
r = requests.post(validateURL, validateDict)

