import pandas
import statistics

def mean(list):
    sum = 0
    for x in list:
        sum = sum + x         
    return (sum/len(list))

def printlist(list):
    for x in list:
        print(x)

def readCSV():
    path = "acnwala-friendscount.csv"
    colnames = ["USER", "FRIENDCOUNT"]
    data = pandas.read_csv(path, names=colnames)
    fcount = data.FRIENDCOUNT.tolist()
    users = data.USER.tolist()
    #Remove header titles
    fcount.pop(0)
    users.pop(0)
    #String to Integer
    fcount = list(map(int, fcount))
    printlist(sorted(fcount))
    print("Mean    = ",mean(fcount))
    print("Median  = ",statistics.median(fcount))
    print("Std Dev = ",statistics.stdev(fcount))


readCSV()
