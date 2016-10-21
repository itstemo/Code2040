import requests
import json

prefixUrl = 'http://challenge.code2040.org/api/prefix'
prefixDict = {'token': '5704643fa526b42f42e46f97740539a4'}

r = requests.post(prefixUrl, prefixDict)

postDictionary = r.json()

prefix = postDictionary['prefix']
wordsArray = postDictionary['array']

print(prefix)
print(wordsArray)
notPrefixStringsArray = []

for string in wordsArray:
	if not (string.startswith( prefix )):
		notPrefixStringsArray.append(string)


print(notPrefixStringsArray)

#Necessary for POSTing the arrays string
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

validateUrl = 'http://challenge.code2040.org/api/prefix/validate'
validateDict = {'token' : '5704643fa526b42f42e46f97740539a4' , 'array' : notPrefixStringsArray }

r = requests.post(validateUrl, data=json.dumps(validateDict), headers=headers)