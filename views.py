from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Book


class BookListView(ListView):
    model = Book
    template_name = "myquill/book_list.html"  # Optional: defaults to book_list.html
    context_object_name = "books"  # Optional: defaults to object_list


class BookDetailView(DetailView):
    model = Book
    template_name = "myquill/book_detail.html"  # Optional: defaults to book_detail.html
    context_object_name = "book"  # Optional: defaults to object


class BookCreateView(CreateView):
    model = Book
    fields = ["name", "properties"]
    template_name = "myquill/book_form.html"  # Optional: defaults to book_form.html
    success_url = reverse_lazy("book-list")


class BookUpdateView(UpdateView):
    model = Book
    fields = ["name", "properties"]
    template_name = "myquill/book_form.html"  # Reuses the create form template
    success_url = reverse_lazy("book-list")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "myquill/book_confirm_delete.html"  # Optional: defaults to book_confirm_delete.html
    success_url = reverse_lazy("book-list")