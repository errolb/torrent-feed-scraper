#!/usr/bin/env python

"""
PROGRAM OUTLINE
===============
    return list of feeds from JSON file
    iterate through the feeds
    download any undownloaded torrent files
===============
"""

import feedparser
import pprint
import urllib
try:
    import json
except ImportError:
    import simplejson as json
import socket

#for if download hangs / site takes too long to respond. Hope timeout works
socket.setdefaulttimeout(10)

#feed file location.
json_file = "/home/narkath/.torrent_scraper/feed_list.json"
#Change this to where you have your torrent client watching.
watch_location = "/home/narkath/Downloads/_watch/"

#json feed getter function
def getlist(json_file):
    with open(json_file) as f:
        file_contents = json.load(f)
        f.close()
    return file_contents


#torrent downloader function ... utilizing data from RSS URL
def download(entry):
    for x in range(0, len(entry)): 
        try:
            with open(watch_location + entry[x].title + ".torrent.added") as f: pass
            print ".torrent " + entry[x].title + " has already been added"
        except IOError as e:
            urllib.urlretrieve(entry[x].link, watch_location + entry[x].title + ".torrent")
            print "Downloading .torrent file " + entry[x].title


jsondata = getlist(json_file)
#iterate through feed entries
for entry in jsondata['rss']:
    print "Accessing feed '" + entry['feedTitle'] + "' : " + entry['feedUrl'] + " ..."
    #return XML data
    xmldata = feedparser.parse(entry['feedUrl'])
    #turn xml useable data
    feeddata = xmldata.entries
    #download torrent files from feed data
    print "Attempting to download related .torrent files ..."
    download(feeddata)

