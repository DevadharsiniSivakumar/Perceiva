import csv
import pyttsx3

# Initialize TTS
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Load books and search
def get_book_location(title):
    try:
        with open("books.csv", newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Title'].strip().lower() == title.strip().lower():
                    return row['Shelf Number']
    except FileNotFoundError:
        speak("CSV file not found.")
        return None
    return None

# Input from user
if __name__ == "__main__":
    book_title = input("Enter the book title: ")
    location = get_book_location(book_title)
    
    if location:
        message = f"The book '{book_title}' is located on shelf number {location}."
    else:
        message = f"Sorry, the book '{book_title}' was not found in the database."

    print(message)
    speak(message)
