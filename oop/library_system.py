class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int):
        super().__init__(title, author)
        self.file_size = file_size  

    def __str__(self):
        return f"{super().__str__()} [E-Book, File Size: {self.file_size}MB]"
    
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{super().__str__()} [Print Book, Pages: {self.page_count}]"
    
class Library:
    def __init__(self):
        self.books = []  

    def add_book(self, book: Book):
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book or its subclasses can be added to the library.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Library Collection:")
            for book in self.books:
                print(f"- {book}")

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()