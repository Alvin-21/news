import urllib.request, json
from .models import Article, Source

# Getting api key
api_key = None
# Getting the news base url
base_url = None
#Getting the article base url
article_url = None
# Getting the topheadline url
topheadline_url = None

def configure_request(app):
    global api_key, base_url, article_url, topheadline_url
    api_key = app.config["NEWS_API_KEY"]
    base_url = app.config["SOURCE_BASE_URL"]
    article_url = app.config["ARTICLE_BASE_URL"]
    topheadline_url = app.config["TOP_HEADLINES_URL"]

    