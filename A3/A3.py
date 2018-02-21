import urllib.request
from urllib.request import Request, urlopen
from requests.exceptions import HTTPError
from socket import error as SocketError
from http.cookiejar import CookieJar
import requests
import json
import lxml


import justext
filelist = []

def getHTML():

    x = 0

    path = "/home/tim/Documents/anwala.github.io-master/A3/html/file"
    

    with open("output.txt","r") as file:
        for url in file :
            x=x+1
            print(x)            
            try:
                data = urllib.request.urlopen(url,timeout = 8)
                print("STATUS CODE:",data.getcode())
                outfile = open(path+str(x),"wb")
                outfile.write(data.read())
                outfile.close()

            except urllib.error.URLError as e: 
                ResponseData = e.read().decode("utf8", 'ignore')
            except socket.timeout:
                logging.error('socket timed out - URL %s')

       

    
def getText():

    path = "/home/tim/Documents/anwala.github.io-master/A3/text/text"
    x=0    
    with open("output.txt","r") as file:
        for url in file :
            x=x+1
            try:
                response = requests.get(url)               
                if response.content is not None:
                    print(x)
                    paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
                    for paragraph in paragraphs:
                        
                        if not paragraph.is_boilerplate:
                            outfile = open(path+str(x),"w")
                            outfile.write(paragraph.text)
                            outfile.close()
                

            except requests.exceptions.ConnectionError:
                response.status_code = "Connection refused"


            except UnicodeDecodeError:
                print("Unicode Error")
            except:
                print("Error")

getText()



