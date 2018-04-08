#!/usr/bin/python
# -*- coding: utf-8 -*-
import feedparser
import re
from feedgen.feed import FeedGenerator
# feedgen is used to convert blogs to RSS feeds



def getwordcounts(url):
    '''
    Returns title and dictionary of word counts for an RSS feed
    '''
    # Parse the feed
    d = feedparser.parse(url)
    wc = {}

    # Loop over all the entries
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary

        else:
            summary = e.description

        # Extract a list of words
        words = getwords(e.title + ' ' + summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word] += 1

    return (d.feed.title, wc)


def getwords(html):
    # Remove all the HTML tags
    txt = re.compile(r'<[^>]+>').sub('', html)

    # Split words by all non-alpha characters
    words = re.compile(r'[^A-Z^a-z]+').split(txt)

    # Convert to lowercase
    return [word.lower() for word in words if word != '']



path = "/home/tim/Documents/A7/"




apcount = {}
wordcounts = {}



feedlist = [line for line in open(path + 'newfeeds.txt')]


i=0
for feedurl in feedlist:
   for feedurl in feedlist:
    try:

        url_title = feedurl.replace("http://","")
        url_title = url_title.replace("www","")
        url_title = url_title.replace("com","")
        url_title = url_title.replace("/","")
        url_title = url_title.replace(".","")
        
        feedurl=feedurl.replace('"','')


        i+=1


        (url_title,wc) = getwordcounts(feedurl)

        wordcounts[url_title] = wc
        for (word, count) in wc.items():
            apcount.setdefault(word, 0)
            if count > 1:
                apcount[word] += 1
        print("True")
    except:
        print('Failed to parse feed %s' % feedurl)


wordlist = []
for (w, bc) in apcount.items():
    frac = float(bc) / len(feedlist)
    if frac > 0.1 and frac < 0.5:
        wordlist.append(w)


out = open(path + 'blogdata.txt', 'w')
out.write('Blog')
for word in wordlist:
    out.write('\t%s' % word)



out.write('\n')

for (blog, wc) in wordcounts.items():
    print(blog)
    out.write(blog)
    print("length ",len(wordlist))
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else:
            out.write('\t0')
    out.write('\n')

