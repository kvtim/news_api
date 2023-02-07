from django.core.validators import MinLengthValidator
from django.db import models


class Country(models.Model):
    id = models.CharField(max_length=2, primary_key=True, validators=[MinLengthValidator(limit_value=2)])
    name = models.CharField(max_length=150, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'


class News(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Title')
    description = models.TextField(verbose_name='Description')
    content = models.TextField(verbose_name='Content')
    source_url = models.CharField(max_length=1000, verbose_name='Source url')
    image_url = models.CharField(blank=True, max_length=1000, verbose_name='Image url')
    published_at = models.DateTimeField(verbose_name='Published time')

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        verbose_name='Country'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Parsing(models.Model):
    parsing_time = models.DateTimeField(verbose_name='Parsing time')

    def __str__(self):
        return self.parsing_time
