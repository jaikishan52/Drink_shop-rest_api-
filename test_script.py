import requests #pip3 install requests
import json 
#pip3 install flask

response = requests.get('https://api.stackexchange.com/2.3/answers?order=desc&sort=activity&site=stackoverflow')


for data in  response.json()['items']:
  #print(data['owner']["display_name"])
  print(data['owner']["link"])

