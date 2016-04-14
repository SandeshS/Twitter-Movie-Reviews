from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
import json
from pprint import pprint

headers = {
	'Accept' : 'application/json'
}

responsebody = urlopen(request).read()
#print responsebody
data = json.loads(responsebody)
#pprint(data)
for item in data[u'results']:
	if item[u'popularity'] > 5:
		print item[u'title']
