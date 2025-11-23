import os
from books import Book

FILE_NAME="library_data.txt"
class Library:
    def __init__(self):
        self.books = []
        self.load_books_from_file()
    def add_book(self, book_id, title, author):
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        self.save_books_to_file()
        print(f"Success:'{title}' added to library")
    def list_books(self):
        print("\n---Current Library Books---")
        if not self.books:
            print("No books available")
        for book in self.books:
            print(book)

        print("-------------------")
    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_available:
                    book.is_available = False
                    self.save_books_to_file()
                    print(f"You have borrowed '{book.title}' book")
                    return
                else:
                    print(f"sorry, book '{book.title}' is alraedy borrowed")
                    return
                print("Error:Book ID not found.")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_available:
                    book.is_available = True
                    self.save_books_to_file()
                    print(f"you have returned '{book.title}' book")
                    return
                else:
                    print(f"error:'{book.title}'was not borrowed")
                    return
    print("error:book ID not found.")

    def save_books_to_file(self):
        try:
            with open(FILE_NAME, "w") as f:
                for book in self.books:
                    f.write(book.to_csv_format())
        except Exception as e:
            print(f"Error saving books to file: {e}")
    def load_books_from_file(self):
        if not os.path.exists(FILE_NAME):
            return
        try:
            with open(FILE_NAME, "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) == 4:
                        self.books.append(Book(int(data[0]), data[1], data[2],data[3]))
        except Exception as e:
            print(f"Error loading books from file: {e}")








