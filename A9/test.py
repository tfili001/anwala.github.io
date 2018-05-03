import numpredict
import numpy as np
path = "/home/tim/Documents/A9/out.txt"




data = open(path).read()
data = [item.split() for item in data.split('\n')[:-1]]



for x in data:
     data = list(map(int, x))


#print(data)

print(str(type(data)))

numpredict.knnestimate(data,(95,15))
#x = numpredict.cosine_sim(data,(95.0,15.0))



