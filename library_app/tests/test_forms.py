from django.test import SimpleTestCase
from book_library.forms import BookForm


class TestForms(SimpleTestCase):

    def test_book_form_valid_data(self):
        form = BookForm(data={
            'title': 'title_1',
            'author': 'author_1',
            'pub_year': 1234,
            'isbn': 1234567890,
            'page_count': 234,
            'cover_url': 'https://www.example.com',
            'lang': 'en'
        })
        self.assertTrue(form.is_valid())

    def test_form_no_data(self):
        form = BookForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 7)
