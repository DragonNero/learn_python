from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

link0 = input('Enter - ')
timesFollowLink = 7
urlList = list()
urlList.append(link0)

for x in range(0, timesFollowLink):

    html = urlopen(urlList[x], context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    print('URL:', tags[17].get('href', None))

    myNewLink = tags[17].get('href', None)
    urlList.append(myNewLink)


print(urlList[timesFollowLink])
