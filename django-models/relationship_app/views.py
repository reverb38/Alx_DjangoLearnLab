from django.shortcuts import render
from .models import Book, Library

# Function-based view
def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'list_books.html', {'books': books})

# Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
   
