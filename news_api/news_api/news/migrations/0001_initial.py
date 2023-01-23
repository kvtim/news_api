# Generated by Django 4.1.3 on 2022-11-26 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Parsing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parsing_time', models.DateTimeField(verbose_name='Parsing time')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('content', models.TextField(verbose_name='Content')),
                ('source_url', models.CharField(max_length=150, verbose_name='Source url')),
                ('image_url', models.CharField(blank=True, max_length=150, verbose_name='Image url')),
                ('published_at', models.DateTimeField(verbose_name='Published time')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.country', verbose_name='Country')),
            ],
        ),
    ]
