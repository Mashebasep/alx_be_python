class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        def __str__(self):
            return f"{self.title} by {self.author}"
        class Ebook(Book):
            def __init__(self, title, author, file_size):
                super().__init__(title, author)
                self.file_size = file_size
                def __str__(self):
                    return f"{super().__str__()} - EBok, file size: {self.file_size} KB"
                class PrintBook(Book):
                    def __init__(self, title, author, page_count):
                        super().__init__(title, author)
                        self.page_count = page_count
                        def __str__(self):
                            return f"{super().__str__()} - Print Book, Page Count: {self.page_count}"
                        class Library:
                            def __init__(self):
                                self.books = []
                                def add_book(self, book):
                                    self.books.append(book)
                                    def list_books(self):
                                        for book in self.books:
                                            print(book)
                                            library = Library()
                                            book1 = Book("To kill a mockingbird", "Harper Lee")
                                            ebook1 = Ebook("1984", "George Orwell", 1024)
                                            print_book1 = PrintBook("The Great Gatsby", "F. Scott Fitzgerald", 200)
                                            library.add_book(book1)
                                            library.add_book(ebook1)
                                            library.add_book(print_book1)
                                            library.list_books()
                                            