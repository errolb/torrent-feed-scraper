torrent-feed-scraper
====================

A simple torrent feed scraper. Pair this with a torrent program that has a watch folder and you have a nifty automated system. 
I created this to run on my headless media server as a cron in conjunction with with transmission daemon.

Requires: http://code.google.com/p/feedparser/

JSON structure as follows ...
====================
{
"rss": [
            {
                "feedTitle": "Feed Name",
                "feedUrl": "http://www.somewebsite.com/?page=rss"
            },
            {
                "feedTitle": "Feed Name 2",
                "feedUrl": "http://www.anotherwebsite.com/?page=rss"
            }
        ]
}
