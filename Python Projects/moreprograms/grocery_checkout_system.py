# Class to represent a Book
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

# Class to represent a Library
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, isbn):
        book_to_remove = None
        for book in self.books:
            if book.isbn == isbn:
                book_to_remove = book
                break
        if book_to_remove:
            self.books.remove(book_to_remove)
            print(f"Book '{book_to_remove.title}' removed from the library.")
        else:
            print("Book not found.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book.display_info())

# Inherited class for specialized Library (Polymorphism)
class SpecialLibrary(Library):
    def add_book(self, book):
        super().add_book(book)
        print(f"Special handling for book '{book.title}'.")

def main():
    # Creating book objects
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("1984", "George Orwell", "0987654321")

    # Creating library object
    my_library = Library()

    # Adding books to the library
    my_library.add_book(book1)
    my_library.add_book(book2)

    # Displaying books in the library
    print("\nBooks currently in the library:")
    my_library.display_books()

    # Removing a book from the library
    my_library.remove_book("1234567890")

    # Displaying books after removal
    print("\nBooks currently in the library after removal:")
    my_library.display_books()

    # Demonstrating inheritance and polymorphism
    special_library = SpecialLibrary()
    special_library.add_book(book1)

if __name__ == "__main__":
    main()
