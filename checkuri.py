import requests
import sys
#   TODO
#Check if links are in twitter domain
#Check if final URI is unique
#Download JSON for step 2
    #Parse into excel

#Download JSON for step 3
    #Parse into excel

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
    fout = open("output.txt","w")
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
