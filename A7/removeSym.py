import sys



def removeSym(sym):
    file = open(sys.argv[1],"r")
    page = file.readlines
    for line in page:
        line.replace(sym,"")


removeSym('"')
