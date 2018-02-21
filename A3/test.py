from bs4 import BeautifulSoup

import urllib.request
def getHTML():
    file = open("test.txt","wb")
    url = "http://streaming.pro-fhi.net/Panoramix-RadioStation"
    try:
        x = urllib.request.urlopen(url)
        print("STATUS CODE:",x.getcode())

        file.write(x.read())

    except urllib.error.URLError as e: 
        print(str(e))  # print error detail (this may not be a timeout after all!)
        ResponseData = e.read().decode("utf8", 'ignore')
        #file.write(x.read())
        #print(ResponseData)
    except urllib.error.HTTPError as e:
        print(str(e))  # print error detail (this may not be a timeout after all!)





getHTML()
