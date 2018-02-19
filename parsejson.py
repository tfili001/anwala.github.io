import os.path
import json
from glob import glob

def parsejson():
    data = []
    i=0
    path = "/home/tim/Documents/CS432/anwala.github.io-master/Ignorethis_A2/p2JSON"
    pattern = os.path.join(path, '*.json')
    for file_name in glob(pattern):
        print(i," ",file_name)
        with open(file_name) as f:
            try:
                print(i)
                data = json.load(f)
                i=i+1
            except:
                print("File Invalid")
                

parsejson()
