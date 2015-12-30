import json

users = json.loads(open('users.json','r').read())

contributers=json.loads(open('contributionSumDict.json','r').read())

locations={}
for user in users:
	_user=dict(user)
	_user['contributions']=contributers[_user['url']]
	if user['location'] in locations.keys():
		locations[user['location']]['users'].append(_user)
		locations[user['location']]['userCount']=locations[user['location']]['userCount']+1
		locations[user['location']]['contributionSum']=locations[user['location']]['contributionSum']+_user['contributions']
	else:
		locations[user['location']]={'userCount':1}
		locations[user['location']]={'contributionSum':_user['contributions']}
		locations[user['location']]['users']=[_user]



locationsList=[]
for k,v in locations.iteritems():
	locationsList.append({'location': k, 'users': v['users'], 'count':v['count']})

locationsSorted=sorted(locationsList, key=lambda k: k['count'], reverse=True)

print len(locationsSorted)

outfile=open('locations.json','w')
outfile.write(json.dumps(locationsSorted))
outfile.close()