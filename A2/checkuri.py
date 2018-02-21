import requests
import sys


def checkURI():
    i=0
    file = open("input.txt","r")
    newURI = file.readlines()
    file.close()
    result = []
    found = set()
# Remove duplicate URI's
    for url in newURI:
        if url not in found:
            found.add(url)
            result.append(url)

    endURI = []
    fout = open("out.txt","w")
    for x in result:
        print("_________________________")
        if "twitter" in x:
            print(i," TWITTER FOUND")
        else:
            i=i+1
            fout.write(x)
            print(i," ",x)  



    fout.close()        
        

checkURI()
