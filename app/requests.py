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

def get_articles(source_id):
    '''
    This is the function that gets the json response to our url request.
    '''

    get_articles_url = article_url.format(source_id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles_list):
    '''
    Function that processes the articles and transforms them to a list of objects.

    Args:
        articles_list: A list of dictionaries that contain article information.

    Returns :
        articles_results: A list of article objects.
    '''

    articles_results = []

    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')

        if urlToImage:
            articles_object = Article(author, title, description, url, urlToImage, publishedAt)
            articles_results.append(articles_object)

    return articles_results