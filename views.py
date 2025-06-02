from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm
from .utils import export_books_to_csv
from django.http import HttpResponse
import csv
from .models import Book

# List of books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})

# Add new book form
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            export_books_to_csv()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'library_app/add_book.html', {'form': form})


# Update an existing book
def update_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            export_books_to_csv()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/add_book.html', {'form': form, 'book': book})

#edit a book
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')  
    else:
        form = BookForm(instance=book)
    return render(request, 'library_app/edit_book.html', {'form': form})

# Delete a book
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        export_books_to_csv()
        return redirect('book_list')
    return render(request, 'library_app/delete_book.html', {'book': book})


def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'

    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'ISBN', 'Shelf Number'])

    for book in Book.objects.all():
        writer.writerow([book.title, book.author, book.isbn, book.shelf_number])

    return response

