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

def process_results(source_list):
    '''
    This is the function  that processes the source result and transform them to a list of Objects.

    Args:
        source_list: A list of dictionaries that contain source details.

    Returns :
        source_results: A list of source objects.
    '''

    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id, name, description, url, category, country)
        source_results.append(source_object)

    return source_results
