# Generated by Django 3.2.9 on 2021-11-19 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Book Title')),
                ('author', models.CharField(max_length=200, verbose_name='Author')),
                ('pub_year', models.DateField(verbose_name='Publication Year')),
                ('isbn', models.CharField(max_length=200, verbose_name='ISBN')),
                ('page_count', models.CharField(max_length=200, verbose_name='Page Count')),
                ('cover_url', models.URLField(default='www.example.com', verbose_name='Cover URL')),
                ('lang', models.CharField(max_length=200, verbose_name='Language')),
            ],
        ),
    ]
