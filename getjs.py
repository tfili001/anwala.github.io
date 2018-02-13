import requests
import json

url = 'http://memgator.cs.odu.edu/timemap/json/'

def getjson():
    i=301
    with open("output.txt", 'r') as input:
       for line in input:
           if i==1000:
               break
           else:
               i=i+1
               print(i," ",line)
               print("test: ",url+line)
               r = requests.get(url+line)


               path = '/home/tim/Documents/anwala.github.io-master/Ignorethis_A2/p2JSON/'+str(i)+'file.json'  

               with open(path, 'wb') as f:
                   f.write(r.content)

getjson()
