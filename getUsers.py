import httplib
import urllib
import json
import time
import base64

headers = {"Content-type": "application/json","Accept":"application/vnd.github.v3+json","User-Agent":"get-github-userinfo"}
userCreds=open('credentials.txt','r').read()
headers['Authorization']='Basic %s' % base64.b64encode(userCreds)

def getUser(url):
	conn = httplib.HTTPSConnection("api.github.com")
	conn.request("GET", url, urllib.urlencode({}), headers)
	response = conn.getresponse()
	if response.status !=200:
		print url, response.read()
		return {}
	data = json.loads(response.read())
	# print data['items'][0]
	conn.close()
	return data

users=[]
for user in json.loads(open('contributionSum.json','r').read()):
	users.append(getUser(user['url']))

outfile=open('users.json','w')
outfile.write(json.dumps(users))
outfile.close()
