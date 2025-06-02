
import csv
import os
from django.conf import settings
from .models import Book

def export_books_to_csv():
    filepath = os.path.join(settings.BASE_DIR, 'books.csv')  # ✅ correct place
    books = Book.objects.all()
    with open(filepath, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'ISBN', 'Shelf Number'])
        for book in books:
            writer.writerow([book.title, book.author, book.isbn, book.shelf_number])
