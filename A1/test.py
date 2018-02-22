import requests
r = requests.get('https://www.youtube.com/')
print(r.status_code)

'''

def checkPDF():
    i = 0
    pdflist = [] 
    for link in links:
        urlretrieve(link, file_path)
        result = magic.from_file(file_path)
        if "PDF" in result:
            i+=1
            pdflist.append(result)
            print(i,result)
'''

