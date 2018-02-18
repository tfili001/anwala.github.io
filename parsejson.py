import os.path
import json
from glob import glob

def parsejson():
    data = []
    i=0
    path = "/home/tim/Documents/anwala.github.io-master/Ignorethis_A2/p2JSON"
    pattern = os.path.join(path, '*.json')
    for file_name in glob(pattern):
        i=i+1
        with open(file_name) as f:
            data.append(json.load(f))
            print(i," ",file_name)

parsejson()

