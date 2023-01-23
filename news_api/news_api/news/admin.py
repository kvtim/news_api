from django.contrib import admin

from .models import Country, News, Parsing

admin.site.register(Country)
admin.site.register(News)
admin.site.register(Parsing)
