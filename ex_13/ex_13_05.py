import urllib.request, urllib.parse, urllib.error
import json
address = 'http://py4e-data.dr-chuck.net/comments_1122017.json'

print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
info = json.loads(data)

print('User count:', len(info))

listCount = list()

for item in info['comments']:
    num = int(item['count'])
    listCount.append(num)
print(listCount)


total = sum(listCount)
print(total)
