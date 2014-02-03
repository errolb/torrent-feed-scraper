torrent-feed-scraper
====================

A simple torrent feed scraper. Pair this with a transmission-daemon and watch folder and you have a nifty automated system. 
I created this to run on my headless media server as a cron job.

Please view [torrent_feed_manager](https://github.com/errolb/torrent_feed_manager) for a little more instruction. As mentioned there, `feed_list.json` needs to be created and the `watch_location` needs to point to where `transmission_daemon` is watching for new .torrent files.

Requires the installation of: http://code.google.com/p/feedparser/

JSON (malformed :/) structure should be as follows ...
====================
```json
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
```
