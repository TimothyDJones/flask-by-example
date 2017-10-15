import sys
import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

# BBC_FEED = "https://feeds.bbci.co.uk/news/rss.xml"
RSS_FEEDS = {
	"bbc": "https://feeds.bbci.co.uk/news/rss.xml",
	"cnn": "https://rss.cnn.com/rss/edition.rss",
	"fox": "https://feeds.foxnews.com/foxnews/latest",
	"tw": "https://tulsaworld.com/news/local",
	"tnn": "https://feeds.thetulsanews.net/rss/22e65fa71bb4cbbc",
	"google": "https://news.google.com/?output=rss",
	"yahoo": "https://news.yahoo.com/rss/"
}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
	# return "No news is good news."
	try:
		feed = feedparser.parse(RSS_FEEDS[publication])
		return render_template("home.html", articles=feed['entries'])
	except:
		ex = sys.exc_info()[0]
		return "<h2>Error: {0}</h2>".format(ex)

if __name__ == "__main__":
	app.run(port=5000, debug=True)
