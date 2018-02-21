import os.path
import json
import requests
from glob import glob

def parsejson():
    data = []
    i=0
    path = "/home/tim/Documents/anwala.github.io-master/Ignorethis_A2/p3JSON"
    pattern = os.path.join(path, '*.json')
    for file_name in glob(pattern):
        i=i+1

        with open(file_name) as f:
            try:
                  
                data = json.load(f)
                uri_date = data['estimated-creation-date']
                uri = data['uri']
                print(i)

            except:
                continue
                
def statuscode():
    i = 0
    statuslist = []
    with open('output.txt') as fp:
        for line in fp:
            i=i+1
            try:
                r=requests.get(line)
                statuslist.append(str(r.status_code))
                print(i)
            except:
                print("Failed Page")

    with open("status_out.txt", mode='wt', encoding='utf-8') as myfile:
        myfile.write('\n'.join(statuslist))
    
statuscode()
#parsejson()
