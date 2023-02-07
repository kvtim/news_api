import os
from news.models import Country


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


def write_country_to_db(country):
    new_country = Country(id=country['id'], name=country['name'])
    new_country.save()


def add_countries():
    countries_from_db = Country.objects.all()
    if countries_from_db:
        return

    for country in countries:
        write_country_to_db(country)

