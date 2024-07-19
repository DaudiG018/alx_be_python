class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Initially, the book is not checked out

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def is_checked_out(self):
        return self._is_checked_out

    def check_out(self):
        self._is_checked_out = True

    def return_book(self):
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
            print(f"Added '{book.get_title()}' by {book.get_author()} to the library.")
        else:
            print("Invalid book object provided.")

    def check_out_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                if not book.is_checked_out():
                    book.check_out()
                    print(f"Checked out '{title}'.")
                else:
                    print(f"'{title}' is already checked out.")
                return
        print(f"'{title}' is not available in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.get_title() == title:
                if book.is_checked_out():
                    book.return_book()
                    print(f"Returned '{title}'.")
                    return
                else:
                    print(f"'{title}' is not checked out.")
                    return
        print(f"'{title}' is not available in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if not book.is_checked_out()]
        if available_books:
            print("Available books:")
            for book in available_books:
                print(f"- '{book.get_title()}' by {book.get_author()}")
        else:
            print("No books available in the library.")

