import httplib
import urllib
import json
import base64

headers = {"Content-type": "application/json","Accept":"application/vnd.github.v3+json","User-Agent":"get-github-userinfo"}
userCreds=open('credentials.txt','r').read()
headers['Authorization']='Basic %s' % base64.b64encode(userCreds)

conn = httplib.HTTPSConnection("api.github.com")
conn.request("GET", "/rate_limit", urllib.urlencode({}), headers)
response = conn.getresponse()
print response.read()