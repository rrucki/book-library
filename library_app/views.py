from django.contrib.sites import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django_filters.rest_framework import DjangoFilterBackend
from datetime import datetime
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.filters import SearchFilter
from library_app.serializers import UserSerializer, GroupSerializer, BookSerializer
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import Book
from book_library.forms import BookForm
import requests


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filter_fields = ('title', 'author', 'pub_year', 'isbn', 'page_count', 'cover_url', 'lang')
    search_fields = ('title', 'author', 'pub_year', 'isbn', 'page_count', 'cover_url', 'lang')


def index(request):
    search_input = request.GET.get('search_input')

    if search_input:
        vector = SearchVector('title', 'author', 'pub_year', 'isbn', 'page_count', 'cover_url', 'lang')
        query = SearchQuery(search_input)
        book_list = Book.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.00001).order_by('-rank')
    else:
        book_list = Book.objects.all()

    template = loader.get_template('index.html')
    context = {
        'book_list': book_list,
    }
    return HttpResponse(template.render(context, request))


def add_new(request):

    context = {
        "form": BookForm()
    }
    if request.method == "POST":
        save_record = Book()
        save_record.title = request.POST.get('title')
        save_record.author = request.POST.get('author')
        save_record.pub_year = request.POST.get('pub_year')
        save_record.isbn = request.POST.get('isbn')
        save_record.page_count = request.POST.get('page_count')
        save_record.cover_url = request.POST.get('cover_url')
        save_record.lang = request.POST.get('lang')
        save_record.save()
    return render(request, 'add_new.html', context=context)


def edit(request, pk):
    edited_book = Book.objects.get(id=pk)
    return render(request, "edit.html", {'Book': edited_book})


def save_changes(request, pk):
    save_book = Book.objects.get(id=pk)
    form = BookForm(request.POST, instance=save_book)
    if form.is_valid():
        form.save()
        return redirect('/library_app/')
    return render(request, "edit.html", {'Book': save_book})


def delete(request, pk):
    book = Book.objects.get(id=pk)
    book.delete()
    return redirect('/library_app/')


def api(request):
    keywords = request.GET.get('keywords')
    book_list = []
    if keywords:
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=' + str(keywords))
        response = response.json()
        data = response['items']

        for every in data:
            id_j = every['id']
            every = every['volumeInfo']

            try:
                title_j = every['title']
            except KeyError:
                title_j = "N/A"

            try:
                author_j = every['authors'][0]
            except KeyError:
                author_j = "N/A"

            try:
                d = datetime.strptime(every['publishedDate'], '%Y-%m-%d')
                pub_year_j = d.year
            except ValueError:
                pub_year_j = every['publishedDate']
            except KeyError:
                pub_year_j = "N/A"

            try:
                isbn_j = every["industryIdentifiers"][1]["identifier"]
            except KeyError:
                try:
                    isbn_j = every["industryIdentifiers"][0]["identifier"]
                except KeyError:
                    isbn_j = "N/A"

            try:
                page_count_j = every['pageCount']
            except KeyError:
                page_count_j = "N/A"

            try:
                cover_url_j = every['imageLinks']['thumbnail']
            except KeyError:
                try:
                    cover_url_j = every['imageLinks']['smallThumbnail']
                except KeyError:
                    cover_url_j = "N/A"

            lang_j = every['language']
            x = {
                "id": id_j,
                "title": title_j,
                "author": author_j,
                "pub_year": pub_year_j,
                "isbn": isbn_j,
                "page_count": page_count_j,
                "cover_url": cover_url_j,
                "lang": lang_j
            }
            book_list.append(x)
        else:
            pass

    return render(request, 'api.html', {'response': book_list})
