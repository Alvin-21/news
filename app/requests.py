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

def get_source(category):
    '''
    Function that gets the json response to the url request.
    '''
    get_source_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results = process_results(source_results_list)

    return source_results

