import requests
import datetime
import time

getUrl = 'http://challenge.code2040.org/api/dating'

tokenDict = {'token' : '5704643fa526b42f42e46f97740539a4'}

r = requests.post(getUrl, tokenDict)

dateDictionary = r.json()
datestamp = dateDictionary['datestamp']
interval = dateDictionary['interval']

print (datestamp)


time_obj = datetime.datetime.strptime(datestamp[:19], '%Y-%m-%dT%H:%M:%S') #ignores the timezone
print(time_obj)

updatedTime = time_obj + datetime.timedelta(seconds=interval) 
dateAsString = updatedTime.isoformat()

#to avoid importing another library, assumes UTC timezone and adds a Z at the end.
dateWithTimezone =  dateAsString + 'Z' 
print(interval)
print(dateWithTimezone)

validateURL = 'http://challenge.code2040.org/api/dating/validate'
validateDict = {'token': '5704643fa526b42f42e46f97740539a4', 'datestamp': dateWithTimezone }

r = requests.post(validateURL,validateDict)
