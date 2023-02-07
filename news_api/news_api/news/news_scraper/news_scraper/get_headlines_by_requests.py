import datetime
import os

from news.models import News, Country, Parsing
import requests


def get_top_headlines(country):
    api_key = os.environ.get('API_KEY')
    headlines = []
    page = 1
    while True:
        headline = requests.get(
            url=f'https://newsapi.org/v2/top-headlines?country={country.id}&'
                f'page={page}&'
                f'apiKey={api_key}').json()['articles']

        if not headline:
            return headlines

        page += 1
        headlines.extend(headline)


def write_headlines_to_db(headlines_articles, country):
    for article in headlines_articles:
        article['title'] = article['title'].replace("'", "''")
        article['description'] = article['title'].replace("'", "''")
        article['content'] = article['title'].replace("'", "''")

        new_article = News(title=article['title'], description=article['description'],
                           content=article['content'], source_url=article['url'],
                           image_url=article['urlToImage'] if article['urlToImage'] else 'no image',
                           published_at=article['publishedAt'],
                           country=country)
        new_article.save()


def add_news():
    countries = Country.objects.all()

    news = News.objects.all()
    news.delete()

    headlines = [
        {
            'country': country,
            'articles': get_top_headlines(country)
        }
        for country in countries]

    for headline in headlines:
        write_headlines_to_db(headline['articles'], headline['country'])

    current_parsing_time = Parsing(parsing_time=datetime.datetime.now())
    current_parsing_time.save()
