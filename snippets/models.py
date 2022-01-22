from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.core.validators import MaxValueValidator, MinValueValidator
from library_app.models import this_year

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    title = models.CharField('Book Title', max_length=200)
    author = models.CharField('Author', max_length=50)
    pub_year = models.IntegerField('Publication Year', validators=[MaxValueValidator(this_year)])
    isbn = models.PositiveIntegerField('ISBN',
                                       validators=[MinValueValidator(999999999), MaxValueValidator(9999999999999)])
    page_count = models.PositiveIntegerField('Page Count')
    cover_url = models.URLField('Cover URL', default='www.example.com')
    lang = models.CharField('Language', max_length=2)
