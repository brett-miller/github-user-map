import httplib
import urllib
import json
import time
import base64

headers = {"Content-type": "application/json","Accept":"application/vnd.github.v3+json","User-Agent":"get-github-userinfo"}
userCreds=open('credentials.txt','r').read()
headers['Authorization']='Basic %s' % base64.b64encode(userCreds)

def getRepos(pageNumber):
	conn = httplib.HTTPSConnection("api.github.com")
	conn.request("GET", "/search/repositories?q=node.js+language:JavaScript&sort=stars&order=desc&per_page=100&page=pageNumber"+str(pageNumber), urllib.urlencode({}), headers)
	response = conn.getresponse()
	print 'getRepos',response.status, response.reason
	if response.status !=200:
		print response.read()
		return []
	data = json.loads(response.read())
	conn.close()
	return data['items']

def getContributers(url):
	conn = httplib.HTTPSConnection("api.github.com")
	conn.request("GET", url, urllib.urlencode({}), headers)
	response = conn.getresponse()
	print 'getContributers',response.status, response.reason
	if response.status !=200:
		print response.read()
		return []
	users = json.loads(response.read())
	conn.close()
	return users

allUsers=[]
repos={}
for index in range(0,5):
	newRepos=getRepos(index)
	for repo in newRepos:
		repos[repo['url']]=repo
		users=getContributers(repo['contributors_url'])
		repos[repo['url']]['contributers']=users
		allUsers.extend(users)
		time.sleep(.1)

outfile=open('allRepos.json','w')
outfile.write(json.dumps(repos))
outfile.close()

outfile=open('allContributers.json','w')
outfile.write(json.dumps(allUsers))
outfile.close()