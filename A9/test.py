import numpredict

path = "/home/tim/Documents/A9/blogdata_num.txt"
list = open(path).readlines()
data = ''.join(list) # converting list into string

#data = data.decode("utf-8") # Decode the bytes into a useful string
    # Now split the string over all whitespace, then join it together again.
data = ' '.join(data.split())

num = float(data)






#  	 euclidean(v1,v2):

#  	 getdistances(data,vec1,k=5):

#  	 knnestimate(data,vec1,k=1):


numpredict.knnestimate(num,(95.0,15.0))
