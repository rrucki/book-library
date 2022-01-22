# Generated by Django 4.0 on 2022-01-22 12:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0007_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_year',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(2022)], verbose_name='Publication Year'),
        ),
    ]