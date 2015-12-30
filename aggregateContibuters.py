import json

allContributers = json.loads(open('allContributers.json','r').read())

contributionSum={}
for contributer in allContributers:
	if contributer['url'] in contributionSum.keys():
		contributionSum[contributer['url']]=contributionSum[contributer['url']]+contributer['contributions']
	else:
		contributionSum[contributer['url']]=contributer['contributions']

contributionSums=[]
for k,v in contributionSum.iteritems():
	contributionSums.append({'url': k, 'contributions': v})


contributionSumsSorted=sorted(contributionSums, key=lambda k: k['contributions'], reverse=True)

print len(contributionSumsSorted)

outfile=open('contributionSumDict.json','w')
outfile.write(json.dumps(contributionSum))
outfile.close()

outfile=open('contributionSumList.json','w')
outfile.write(json.dumps(contributionSumsSorted))
outfile.close()