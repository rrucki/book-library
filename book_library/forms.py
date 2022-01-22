from django import forms
from library_app.models import Book


class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    author = forms.CharField(max_length=50)
    pub_year = forms.IntegerField()
    isbn = forms.IntegerField()
    page_count = forms.IntegerField()
    cover_url = forms.URLField()
    lang = forms.CharField(max_length=2)

    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'pub_year',
            'isbn',
            'page_count',
            'cover_url',
            'lang'
        ]
