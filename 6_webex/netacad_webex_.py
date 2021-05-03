import requests

#token requested through developer.webex website - 12 hours
#create room 
access_token = '*****'
url = 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}
params={'title': 'netacad_devasc_skills_JB'}
res = requests.post(url, headers=headers, json=params)

#add user to group
room_id = res.json()['id']
person_email = 'yvan.rooseleer@biasc.be'
url = 'https://webexapis.com/v1/memberships'
param = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=param)

#sent message
message = 'JB github: \n https://github.com/jol-knu/Devasc_Skills_JB.git'
url = 'https://webexapis.com/v1/messages'
para = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=para)

#sent attachment to space
text = 'code to create room'
file = "https://github.com/jol-knu/Devasc_Skills_JB/blob/master/example.png?raw=true"
url = 'https://webexapis.com/v1/messages'
par = {'roomId': room_id, 'markdown': text, 'files': file}
res = requests.post(url, headers=headers, json=par)

#sent attachment to space
text = 'bash script output screenshot to webex'
file = "https://github.com/jol-knu/Devasc_Skills_JB/blob/master/bash_output.PNG?raw=true"
url = 'https://webexapis.com/v1/messages'
par = {'roomId': room_id, 'markdown': text, 'files': file}
res = requests.post(url, headers=headers, json=par)
print(res.json())