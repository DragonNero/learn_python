import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET


address = 'http://py4e-data.dr-chuck.net/comments_1122016.xml'

print('Retrieving', address)
uh = urllib.request.urlopen(address)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data.decode())

counts = tree.findall('.//count')
tagList = list()
for count in counts:
    print(count.text)
    num = int(count.text)
    tagList.append(num)
print(tagList)
total = sum(tagList)
print(total)
