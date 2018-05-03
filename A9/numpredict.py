from random import random,randint
import math

def euclidean(v1,v2):
  d=0.0
  for i in range(len(v1)):
    d+=(v1[i]-v2[i])**2
  return math.sqrt(d)

def getdistances(data,vec1,k=5):
  distancelist=[]
  
  # Loop over every item in the dataset
  for i in range(len(data)):
    vec2=data[i]
    
    # Add the distance and the index
    distancelist.append((euclidean(vec1,vec2),i))
  
  # Sort by distance
  distancelist.sort()
  return distancelist

def knnestimate(data,vec1,k=1):
  # Get sorted distances
  dlist=getdistances(data,vec1)
  avg=0.0
  
  # Take the average of the top k results
  for i in range(k):
    idx=dlist[i][1]
    avg+=data[idx]['result']
  avg=avg/k
  return avg


def cosine_sim(data,a):
    sum_magA = 0
    sum_magB = 0
    sumAB = 0
    for i in range(len(data)):
        b=data[i][0]
    for i in range(len(data)):
        sumAB += a[i]*b[i]
        sum_magA += pow(a[i],2)
        sum_magB += pow(b[i],2)
    sum_magA = sqrt(sum_magA)
    sum_magB = sqrt(sum_magB)
    return sumAB/(sum_magA*sum_magB)
    

    
    
