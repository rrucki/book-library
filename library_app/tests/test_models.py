from django.test import TestCase
from library_app.models import Book


class TestModels(TestCase):

    def setUp(self):
        self.b1 = Book.objects.create(
            id='1',
            title='title_1',
            author='author_1',
            pub_year=1234,
            isbn=1234567890,
            page_count=123,
            cover_url='https://www.example.com',
            lang='en'
        )

    def test_book_creation(self):
        self.assertEquals(self.b1.title, 'title_1')
        self.assertEquals(self.b1.author, 'author_1')
        self.assertEquals(self.b1.pub_year, 1234)
        self.assertEquals(self.b1.isbn, 1234567890)
        self.assertEquals(self.b1.page_count, 123)
        self.assertEquals(self.b1.cover_url, 'https://www.example.com')
        self.assertEquals(self.b1.lang, 'en')
