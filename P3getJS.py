import os.path
import json
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
                    print(data['estimated-creation-date'])
                    print(i)
                    if "" in data['estimated-creation-date']:
                        print("No estimation date")
            except:
                continue
                

parsejson()
