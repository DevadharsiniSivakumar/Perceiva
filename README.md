# Library Management System

A simple yet powerful library management system built with Django that helps librarians manage their book inventory efficiently.

## Features

- **Book Management**: Add, edit, and delete books from the library inventory
- **Book Listing**: View all books in a clean, sortable table format
- **CSV Export**: Download the entire book catalog as a CSV file
- **Voice Assistant**: Built-in voice assistant to help locate books by shelf number
- **Responsive Design**: Works on desktop and mobile devices

## Technologies Used

- **Backend**: Django 5.2
- **Frontend**: Bootstrap 5
- **Database**: SQLite (default)
- **Voice Assistant**: pyttsx3 for text-to-speech functionality

## Installation

1. Clone the repository
   ```
   git clone https://github.com/DevadharsiniSivakumar/Perceiva
   cd Perceiva
   ```

2. Create and activate a virtual environment
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```
   pip install -r requirements.txt
   ```

4. Run migrations
   ```
   python manage.py migrate
   ```

5. Create a superuser (admin)
   ```
   python manage.py createsuperuser
   ```

6. Start the development server
   ```
   python manage.py runserver
   ```

7. Open your browser and navigate to http://127.0.0.1:8000/

## Usage

### Adding Books
1. Click on the "Add New Book" button
2. Fill in the book details (title, author, ISBN, shelf number)
3. Click "Add Book" to save

### Editing Books
1. Find the book in the list
2. Click the "Edit" button
3. Update the information
4. Click "Update Book" to save changes

### Exporting Data
1. Click the "Download CSV" button to export the entire book catalog

### Using the Voice Assistant
1. Run the book finder assistant
   ```
   python book_finder_assistant.py
   ```
2. Enter the book title when prompted
3. The assistant will speak the shelf location of the book

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Future Enhancements

- Barcode scanning for quick book lookup
- Member management system
- Book checkout and return tracking
- Overdue notifications
- Advanced search functionality
