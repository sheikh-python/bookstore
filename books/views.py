from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


class BookCreateView(generic.CreateView):
    model = Book
    template_name = 'books/book_create.html'
    fields = ['title', 'author', 'description', 'price']


class BookUpdateView(generic.UpdateView):
    model = Book
    template_name = 'books/book_update.html'
    fields = ['title', 'author', 'description', 'price']
