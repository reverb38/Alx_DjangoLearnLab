import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

"List all books in a library."
library_name = "Central Library"  # Replace with the actual library name
[library = Library.objects.get(name=library_name)]
library_books = library.books.all()
print(f"Books in {library.name}: {[book.title for book in library_books]}")



# --- Query 2: All books by a specific author ---
author_name = "J.K. Rowling"  # Replace with the actual author name
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()
print(f"Books by {author.name}: {[book.title for book in books_by_author]}")



# --- Query 3: Retrieve the librarian for a library ---
library_name = "Central Library"  # Replace with the actual library name
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")
