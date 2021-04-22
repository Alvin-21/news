from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_articles, get_source, get_topheadlines

# Views
@main.route('/')
def index():
    '''
    Function that returns the index page and its data.
    '''

    business_news = get_source("business")
    entertainment_news = get_source("entertainment")
    general_news = get_source("general")
    health_news = get_source("health")
    science_news = get_source("science")
    sports_news = get_source("sports")
    technology_news = get_source("technology")

    title = "Home | News Sources"

    return render_template('index.html', title=title, business=business_news, entertainment=entertainment_news, general=general_news, health=health_news, science=science_news, sports=sports_news, technology=technology_news)

@main.route('/articles/<source_id>')
def articles(source_id):
    '''
    Function that returns the source's articles.
    '''

    article_source = get_articles(source_id)

    title = f"{source_id} Articles"
    
    return render_template('articles.html', title=title, articles=article_source)

@main.route('/topheadlines')
def topheadlines():
    '''
    Function that returns top headline articles.
    '''

    topheadline_articles = get_topheadlines()

    title = 'Top Headlines'

    return render_template('topheadlines.html', title=title, articles = topheadline_articles)