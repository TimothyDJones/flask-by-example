import sys
import feedparser
from flask import Flask

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
		first_article = feed['entries'][0]
		print(first_article)
		return """
			<html>
				<body>
					<h1> Headlines </h1>
					<b>{0}</b><br />
					<i>{1}</i><br />
					<p>{2}</p><br />
				</body>
			</html>
		""".format(first_article.get("title"),
			first_article.get("published"),
			first_article.get("summary"))
	except:
		ex = sys.exc_info()[0]
		return "<h2>Error: {0}</h2>".format(ex)

if __name__ == "__main__":
	app.run(port=5000, debug=True)
