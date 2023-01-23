import psycopg2 as psycopg2
from psycopg2 import Error

countries = [
    {
        'id': 'de',
        'name': 'Germany'
    },
    {
        'id': 'lt',
        'name': 'Lithuania'
    },
    {
        'id': 'lv',
        'name': 'Latvia'
    },
    {
        'id': 'fr',
        'name': 'France'
    },
    {
        'id': 'pl',
        'name': 'Poland'
    },
    {
        'id': 'us',
        'name': 'United States'
    },
    {
        'id': 'ca',
        'name': 'Canada'
    },
    {
        'id': 'ru',
        'name': 'Russia'
    }
]


def write_country_to_db(connection, cursor, country):
    insert_query = f""" INSERT INTO news_country (id, name) VALUES ('{country['id']}', '{country['name']}')"""
    cursor.execute(insert_query)
    connection.commit()
    print('Success!')


connection = psycopg2.connect(user="dj_user",
                              password="admin",
                              host="127.0.0.1",
                              port="5432",
                              database="news")

cursor = connection.cursor()

for country in countries:
    write_country_to_db(connection, cursor, country)


if connection:
    connection.close()
    cursor.close()
