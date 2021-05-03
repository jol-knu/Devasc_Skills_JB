import json
import requests
requests.packages.urllib3.disable_warnings()

api_url ="https://192.168.56.101:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/"

headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
           }
basicauth = ("cisco", "cisco123")

data = {"severity": "alerts"}

resp = requests.post(api_url, data=json.dumps(data), auth=basicauth, headers=headers, verify=False)

print(resp)


