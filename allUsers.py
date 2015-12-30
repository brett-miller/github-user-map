import httplib
import urllib
import json
import time
import sys
import base64

if(len(sys.argv) != 2):
	print "Need to the run the program like the following: python allUsers.py CityName"
	sys.exit()
else:
	print "Finding Top github users in the city: " + sys.argv[1]
	print "The results will be stored in JSON files in this directory"

headers = {"Content-type": "application/json","Accept":"application/vnd.github.v3+json","User-Agent":"get-github-userinfo"}
userCreds=open('credentials.txt','r').read().strip()
headers['Authorization']='Basic %s' % base64.b64encode(userCreds)

# headers = {"Content-type": "application/json","Accept":"application/vnd.github.v3+json","User-Agent":"brett-miller"}

def getUsersByParameter(location, sortParam, startPageNumber, endPageNumber, headers):
	conn = httplib.HTTPSConnection("api.github.com")
	users = []
	for j in range(startPageNumber, endPageNumber):
		page = str(j)
		conn.request("GET", "/search/users?q=location:" + location + "&sort=" + sortParam + "&order=desc&page=" + page, urllib.urlencode({}), headers)
		response = conn.getresponse()
		if(response.status != 200):
			print response.read()
		print response.status, response.reason
		data = json.loads(response.read())
		users.extend(data['items'])
		conn.close()
		time.sleep(2)
	return users

def getAllUsersWithParameters(location, startPageNumber, endPageNumber, headers):
	conn = httplib.HTTPSConnection("api.github.com")
	users = []
	users.extend(getUsersByParameter(location, "followers", startPageNumber, endPageNumber, conn, headers))
	users.extend(getUsersByParameter(location, "public_repos", startPageNumber, endPageNumber, conn, headers))
	users.extend(getUsersByParameter(location, "collaborators", startPageNumber, endPageNumber, conn, headers))
	users.extend(getUsersByParameter(location, "owned_private_repos", startPageNumber, endPageNumber, conn, headers))
	users.extend(getUsersByParameter(location, "total_private_repos", startPageNumber, endPageNumber, conn, headers))
	for i in range(len(users)):
		printData = json.dumps(users, sort_keys=True, indent=2, separators=(',', ': '))
		print printData
	

outfile=open('topUserByFollowersByCity.json','w')
outfile.write(json.dumps(getUsersByParameter(sys.argv[1], 'followers', 1, 2, headers)))
outfile.close()

outfile=open('topUserByPublicReposByCity.json','w')
outfile.write(json.dumps(getUsersByParameter(sys.argv[1], 'public_repos', 1, 2, headers)))
outfile.close()

outfile=open('topUserByCollaboratorsByCity.json','w')
outfile.write(json.dumps(getUsersByParameter(sys.argv[1], 'collaborators', 1, 2, headers)))
outfile.close()

outfile=open('topUserByOwnedPrivateReposByCity.json','w')
outfile.write(json.dumps(getUsersByParameter(sys.argv[1], 'owned_private_repos', 1, 2, headers)))
outfile.close()

outfile=open('topUserByTotalPrivateReposByCity.json','w')
outfile.write(json.dumps(getUsersByParameter(sys.argv[1], 'total_private_repos', 1, 2, headers)))
outfile.close()
