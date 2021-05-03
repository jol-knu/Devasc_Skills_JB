import json
import requests
requests.packages.urllib3.disable_warnings()

api_url ="https://192.168.56.101/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity"

headers = {"Accept":"application/yang-data+json",
           "Content-type":"application/yang-data+json"
           }
basicauth = ("cisco", "cisco123")

warconf = {"severity": "warnings"}


resp = requests.put(api_url, data=json.dumps(warconf), auth=basicauth, headers=headers, verify=False)

print(resp)


