from django.test import SimpleTestCase
from django.urls import reverse, resolve
from library_app.views import index, add_new, edit, api, save_changes, delete


class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def test_add_new_url_resolves(self):
        url = reverse('add_new')
        self.assertEquals(resolve(url).func, add_new)

    def test_edit_url_resolves(self):
        url = reverse('edit', args=['1'])
        self.assertEquals(resolve(url).func, edit)

    def test_api_url_resolves(self):
        url = reverse('api')
        self.assertEquals(resolve(url).func, api)

    def test_save_changes_url_resolves(self):
        url = reverse('save_changes', args=['1'])
        self.assertEquals(resolve(url).func, save_changes)

    def test_delete_url_is_resolves(self):
        url = reverse('delete', args=['1'])
        self.assertEquals(resolve(url).func, delete)

