from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

this_year = datetime.today().year


class Book(models.Model):
    title = models.CharField('Book Title', max_length=200)
    author = models.CharField('Author', max_length=50)
    pub_year = models.IntegerField('Publication Year', validators=[MaxValueValidator(this_year)])
    isbn = models.BigIntegerField('ISBN',
                                  validators=[MinValueValidator(999999999), MaxValueValidator(9999999999999)])
    page_count = models.PositiveIntegerField('Page Count')
    cover_url = models.URLField('Cover URL', default='https://www.example.com')
    lang = models.CharField('Language', max_length=2)
