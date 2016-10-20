import requests
import json

url = 'http://challenge.code2040.org/api/reverse'
reverseDictionary = {'token': '5704643fa526b42f42e46f97740539a4'}

stringToReverse = requests.post(url, data=reverseDictionary)

#prepped = stringToReverse.prepare()
print(stringToReverse.text)
reversedString = stringToReverse.text[::-1]
print(reversedString)



dictionaryReversedString = {'token': '5704643fa526b42f42e46f97740539a4' , 'string' : reversedString}
validateURL = 'http://challenge.code2040.org/api/reverse/validate'
r = requests.post(validateURL, data=dictionaryReversedString)