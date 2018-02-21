import os

def getdocker():
    i=0
    with open("out.txt", 'r') as input:
           for link in input:
               if i==1000:
                   break
               else:
                   i=i+1
                  
                   dcmd = """docker run --rm -it oduwsdl/carbondate ./main.py -l search {{URI-R}}""".format(link)
                   fpipe = dcmd + ">> p3file_"+str(i)+".json"
                   os.system(fpipe)
                   print(i,"/1000")
                   


getdocker()
