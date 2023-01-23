import json
import os

import psycopg2
import requests


def get_top_headlines(country):
    api_key = os.environ.get('API_KEY')
    headlines = []
    page = 1
    while True:
        headline = requests.get(
            url=f'https://newsapi.org/v2/top-headlines?country={country}&'
                f'page={page}&'
                f'apiKey={api_key}').json()['articles']

        if not headline:
            return headlines

        page += 1
        headlines.extend(headline)


def load_from_json(country):
    with open(f'headlines_{country}.json', 'r') as rf:
        return json.load(rf)['articles']


def write_headlines_to_db(connection, cursor, headlines_articles, country):
    for article in headlines_articles:
        article['title'] = article['title'].replace("'", "''")
        article['description'] = article['title'].replace("'", "''")
        article['content'] = article['title'].replace("'", "''")
        insert_query = f""" INSERT INTO news_news (title, description, content, 
        source_url, image_url, published_at, country_id) 
        VALUES ('{article['title']}', '{article['description']}', 
        '{article['content']}', '{article['url']}', '{article['urlToImage']}', 
        '{article['publishedAt']}', '{country}')"""

        cursor.execute(insert_query)
        connection.commit()
        print('Success!')


def main():
    connection = psycopg2.connect(user="dj_user",
                                  password="admin",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="news")

    cursor = connection.cursor()

    cursor.execute("SELECT * from news_country")
    countries = cursor.fetchall()
    print("Countries:", countries)
    countries.pop(4)
    headlines = [
        {
            'country': country[0],
            'articles': load_from_json(country[0])
        }
        for country in countries]

    for headline in headlines:
        write_headlines_to_db(connection, cursor, headline['articles'], headline['country'])

    if connection:
        connection.close()
        cursor.close()


if __name__ == '__main__':
    main()
