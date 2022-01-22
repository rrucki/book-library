from django.test import TestCase, Client
from django.urls import reverse
from library_app.models import Book


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')
        self.add_new_url = reverse('add_new')
        self.edit_url = reverse('edit', args=['1'])
        self.save_changes_url = reverse('save_changes', args=['1'])
        self.delete_url = reverse('delete', args=['1'])
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

    def test_index_GET(self):
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertEquals(self.b1.title, 'title_1')
        self.assertTemplateUsed(response, 'index.html')

    def test_add_new_GET(self):
        response = self.client.get(self.add_new_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_new.html')

    def test_edit_GET(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_save_changes_GET(self):
        response = self.client.get(self.save_changes_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')

    def test_delete_GET(self):
        response = self.client.delete(self.delete_url, {'id': '1'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/library_app/')


