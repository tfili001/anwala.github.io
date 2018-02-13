import glob
import json


def parsejson():
    for filename in glob.glob('/home/tim/Documents/anwala.github.io-master/Ignorethis_A2/p2JSON/*.json'):
        print("fname:",filename)

parsejson()
