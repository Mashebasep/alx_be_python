class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        def __str__(self):
                return f"'{self.title}' by {self.author} ({self.year})"
        def __repr__(self):
                return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
        def __del__(self):
            print(f"Book object '{self.title}' has been deleted.")
            my_book = Book("1984", "George Orwell", 1949)
            print(my_book)
            print(repr(my_book))

            

