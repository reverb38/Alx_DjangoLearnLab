import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Query 1: All books by a specific author ---
author = Author.objects.get(name="Author Name")
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")

# --- Query 2: List all books in a library ---
library = Library.objects.get(name="Library Name")
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")

# --- Query 3: Retrieve the librarian for a library ---
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")
