# Generated by Django 3.2.9 on 2021-11-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_alter_book_pub_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.CharField(max_length=200, verbose_name='Publication Year'),
        ),
    ]