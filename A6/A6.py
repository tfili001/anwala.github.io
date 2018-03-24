#!/usr/bin/python
# -*- coding: utf-8 -*-
from math import sqrt
# A dictionary of movie critics and their ratings of a small set of movies
from heapq import nsmallest
# For lowest item in list
import pandas as pd
# Remove seen_list duplicates

import re
# Get between | in u.item
import operator

path='/home/tim/Documents/A6/ml-100k'

critics = {
    'Lisa Rose': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'Superman Returns': 3.5,
        'You, Me and Dupree': 2.5,
        'The Night Listener': 3.0,
    },
    'Gene Seymour': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 3.5,
        'Just My Luck': 1.5,
        'Superman Returns': 5.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 3.5,
    },
    'Michael Phillips': {
        'Lady in the Water': 2.5,
        'Snakes on a Plane': 3.0,
        'Superman Returns': 3.5,
        'The Night Listener': 4.0,
    },
    'Claudia Puig': {
        'Snakes on a Plane': 3.5,
        'Just My Luck': 3.0,
        'The Night Listener': 4.5,
        'Superman Returns': 4.0,
        'You, Me and Dupree': 2.5,
    },
    'Mick LaSalle': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'Just My Luck': 2.0,
        'Superman Returns': 3.0,
        'The Night Listener': 3.0,
        'You, Me and Dupree': 2.0,
    },
    'Jack Matthews': {
        'Lady in the Water': 3.0,
        'Snakes on a Plane': 4.0,
        'The Night Listener': 3.0,
        'Superman Returns': 5.0,
        'You, Me and Dupree': 3.5,
    },
    'Toby': {'Snakes on a Plane': 4.5, 'You, Me and Dupree': 1.0,
             'Superman Returns': 4.0},
}


def sim_distance(prefs, p1, p2):
    '''
    Returns a distance-based similarity score for person1 and person2.
    '''

    # Get the list of shared_items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they have no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in
                         prefs[p1] if item in prefs[p2]])
    return 1 / (1 + sqrt(sum_of_squares))


def sim_pearson(prefs, p1, p2):
    '''
    Returns the Pearson correlation coefficient for p1 and p2.
    '''

    # Get the list of mutually rated items
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    # If they are no ratings in common, return 0
    if len(si) == 0:
        return 0
    # Sum calculations
    n = len(si)
    # Sums of all the preferences
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])
    # Sums of the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])
    # Sum of the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])
    # Calculate r (Pearson score)
    num = pSum - sum1 * sum2 / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0:
        return 0
    r = num / den
    return r


def topMatches(
    prefs,
    person,
    n=5,
    similarity=sim_pearson,
):
    '''
    Returns the best matches for person from the prefs dictionary. 
    Number of results and similarity function are optional params.
    '''

    scores = [(similarity(prefs, person, other), other) for other in prefs
              if other != person]
    scores.sort()
    scores.reverse()
    return scores[0:n]


def getRecommendations(prefs, person, similarity=sim_pearson):
    '''
    Gets recommendations for a person by using a weighted average
    of every other user's rankings
    '''

    totals = {}
    simSums = {}
    for other in prefs:
    # Don't compare me to myself
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        # Ignore scores of zero or lower
        if sim <= 0:
            continue
        for item in prefs[other]:
            # Only score movies I haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                # Similarity * Score
                totals.setdefault(item, 0)
                # The final score is calculated by multiplying each item by the
                #   similarity and adding these products together
                totals[item] += prefs[other][item] * sim
                # Sum of similarities
                simSums.setdefault(item, 0)
                simSums[item] += sim
    # Create the normalized list
    rankings = [(total / simSums[item], item) for (item, total) in
                totals.items()]
    # Return the sorted list
    rankings.sort()
    rankings.reverse()
    return rankings


def transformPrefs(prefs):
    '''
    Transform the recommendations into a mapping where persons are described
    with interest scores for a given title e.g. {title: person} instead of
    {person: title}.
    '''

    result = {}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            # Flip item and person
            result[item][person] = prefs[person][item]
    return result


def calculateSimilarItems(prefs, n=10):
    '''
    Create a dictionary of items showing which other items they are
    most similar to.
    '''

    result = {}
    # Invert the preference matrix to be item-centric
    itemPrefs = transformPrefs(prefs)
    c = 0
    for item in itemPrefs:
        # Status updates for large datasets
        c += 1
        if c % 100 == 0:
            print('%d / %d' % (c, len(itemPrefs)))
        # Find the most similar items to this one
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_distance)
        result[item] = scores
    return result


def getRecommendedItems(prefs, itemMatch, user):
    userRatings = prefs[user]
    scores = {}
    totalSim = {}
    # Loop over items rated by this user
    for (item, rating) in userRatings.items():
        # Loop over items similar to this one
        for (similarity, item2) in itemMatch[item]:
            # Ignore if this user has already rated this item
            if item2 in userRatings:
                continue
            # Weighted sum of rating times similarity
            scores.setdefault(item2, 0)
            scores[item2] += similarity * rating
            # Sum of all the similarities
            totalSim.setdefault(item2, 0)
            totalSim[item2] += similarity
    # Divide each total score by total weighting to get an average
    rankings = [(score / totalSim[item], item) for (item, score) in
                scores.items()]
    # Return the rankings from highest to lowest
    rankings.sort()
    rankings.reverse()
    return rankings


def loadMovieLens():
  # Get movie titles
    movies = {}
    for line in open(path + '/u.item',encoding="ISO-8859-1"):
        (id, title) = line.split('|')[0:2]
        movies[id] = title
  # Load data
    prefs = {}
    for line in open(path + '/u.data'):
        (user, movieid, rating, ts) = line.split('\t')
        prefs.setdefault(user, {})
        prefs[user][movies[movieid]] = float(rating)
    return prefs

def compareUsers(prefs,p1):
    rank_set = []
    i=1
    with open(path + '/u.user') as f:
        for size, l in enumerate(f):
            pass

    #print("Size = ",size)
    f = open(path + '/u.user','r')
    for item in range(0,size+1):
        #print(i)
        rank_set.append([sim_pearson(prefs, str(p1), str(i)),i])
        i+=1      

    highest = sorted(zip(rank_set), reverse=True)[:5]
    print("Most Correlated\n")
    for rank in highest:
        print(rank)

    lowest = nsmallest(5,rank_set)
    print("Least Correlated")
    for rank in lowest:
        print(rank)

def addRatings(rating_list,rec_list):
    f = open(path + '/u.item','r',encoding="ISO-8859-1")
    rating_list = f.readlines()
    end_list = []
    for line in rating_list:
        for x in rec_list:
            if x[1] == line.split("|")[1].split("|")[0]:
                index = int(line.split("|")[0].split("|")[0])
                end_list.append([x[0],index,x[1]])

    return end_list

def notSeen(prefs,p1):
    rec_list = getRecommendations(prefs,p1)
    seen_list = []
    rating_list = []

    f = open(path + '/u.data','r')
    data_list = f.readlines()

    for line in data_list:
        line = line.strip('\n')
        seen_list.append([line.split()[1],line.split()[2]])
    # Remove duplicates
    df = pd.DataFrame(seen_list)
    df = df.drop_duplicates([0])
    seen_no_dup = df.values.tolist()
    # Remove movies seen
    for line in seen_no_dup:
        try:
            del rec_list[int(line[0])]
        except IndexError:
            pass

    f.close()
    end_list = addRatings(rating_list,rec_list)

    highest = sorted(zip(end_list), reverse=True)[:5]

    print("Top 5 Recommended")
    for item in highest:
        print(item)
    
    lowest = nsmallest(5,end_list)
    print("Bottom 5 Recommended")
    for item in lowest:
        print(item)


def displayMaxMin(list,n):
    highest = sorted(zip(list), reverse=True)[:n]
    for item in highest:
        print(item)


def maxminRecommendedFilms(filmID):
    f = open(path + '/u.item','r',encoding="ISO-8859-1")
    max_list = []
    min_list = []
    data_list = f.readlines()
    genre_val = data_list[272]


    genre_val = genre_val[-39:].replace("|", "")
    for line in data_list:
        genre = line[-39:].replace("|", "")

        count = 1
        false_count = 1
        for i in range(0,19):

            if genre[i] == "1" and genre_val[i] == "1":

                if count != 1:
                    max_list=max_list[:-1]
      
                max_list.append([count,genre.strip(),line.split("|")[0].split("|")[0],line.split("|")[1].split("|")[0]])
                count+=1

        if count == 1:
            min_list.append([count,genre.strip(),line.split("|")[0].split("|")[0],line.split("|")[1].split("|")[0]])


    print("Top Recommended")
    displayMaxMin(max_list,5)

    print("Bottom Recommended")
    displayMaxMin(min_list,5)

    print("Genre Val\n",genre_val)

def closestUsers(amount,identity):
    f = open(path + '/u.user','r',encoding="ISO-8859-1")
    data_list = f.readlines()
    for i in range(0,amount):
        for line in data_list:
             count=0
             for a in range(0,3):
                 if identity[a] in line.split("|")[count+1].split("|")[0]:
                     count+=1


             if count == 3:
                 print(line)
                 




prefs = loadMovieLens()


#0100001000000000100

#def getRecommendedItems(prefs, itemMatch, user):
identity = ["23","M","student"]
closestUsers(3,identity)
#compareUsers(prefs,"33")
#notSeen(prefs,"33")
#maxminRecommendedFilms(272)
