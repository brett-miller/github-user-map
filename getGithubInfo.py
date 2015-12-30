import httplib
import urllib
import json

headers = {"Content-type": "application/json","Accept":"application/vnd.github.v3+json","User-Agent":"brett-miller"}

conn = httplib.HTTPSConnection("api.github.com")
conn.request("GET", "/search/repositories?q=npm%20install+language:JavaScript&sort=stars&order=desc", urllib.urlencode({}), headers)
response = conn.getresponse()
print response.status, response.reason
data = json.loads(response.read())
# print data['items'][0]
print data['items'][0]['contributors_url']
conn.close()

conn = httplib.HTTPSConnection("api.github.com")
conn.request("GET", "/repos/Medium/phantomjs/contributors", urllib.urlencode({}), headers)
response = conn.getresponse()
print response.status, response.reason
data = json.loads(response.read())
# print data['items'][0]
print data
conn.close()
