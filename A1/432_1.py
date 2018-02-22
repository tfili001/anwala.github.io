from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import requests
import sys

#http://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7723740
#https://www.odu.edu/compsci

test = sys.argv[1]
links = []

def getLinks(url):
    data = urlopen(url)
    soup = BeautifulSoup(data, 'html.parser')
    for link in soup.find_all('a',href=True):
        inst = link.get('href')
        if inst.startswith("http://"):
            links.append(inst)

def getRedirects():
    print("Redirects")
    for url in links:
        r = requests.head(url,allow_redirects=True)
        if r.url != url:
            links.append(r.url)
            print(url,"\n",r.url,"\nstatus:",r.status_code)
        else:
            print(url,"\n","status:",r.status_code)


def checkPDF():
    pdflist = []
    i = 0
    print("List of PDFs")
    for x in links:
        r = requests.get(x)
        ftype = r.headers['content-type']    
        if "None" in ftype:
            print("None")
            break
        elif "pdf" in ftype:
           pdflist.append(x)
           print("________________________\n",x,"\nSize:",len(r.content),"\nFile type: ",ftype)
    
    if not pdflist:
        print("No PDFs found")
 
getLinks(test)
getRedirects()
checkPDF()



