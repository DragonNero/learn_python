# Search for link values within URL input
import urllib.request, urllib.parse, urllib.error
import re
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link0 = input('Enter - ')

html = urllib.request.urlopen(link0, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
print(links[2].decode())
link1 = links[2].decode()

html = urllib.request.urlopen(link1, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
print(links[2].decode())
link2 = links[2].decode()

html = urllib.request.urlopen(link2, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
print(links[2].decode())
link3 = links[2].decode()

html = urllib.request.urlopen(link3, context=ctx).read()
links = re.findall(b'href="(http[s]?://.*?)"', html)
print(links[2].decode())
link4 = links[2].decode()

print(link4)
