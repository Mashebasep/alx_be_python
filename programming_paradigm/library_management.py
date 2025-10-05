class Book:
    def __init__(self, title, author):
        self.title = title
        self.author= author
        self._is_checked_out = False
        def check_out(self):
            if not self._is_checked_out:
                self._is_checked_out = True
                return True
            return False
        def return_book(self):
            self._is_checked_out = False
            def is_available(self):
                return not self._is_checked_out
            class Library:
                def __init__(self):
                    self._books = []
                    def add_book(self, book):
                        self._books.append(book)
                        print(f'Book added: "{book.title}" by {book.author}')
                        def check_out_book(self, title):
                            for book in self._books:
                                if book.title.lower() == title.lower():
                                    if book.check_out():
                                        print(f'You have checked out "{book.title}".')
                                        return
                                    else:
                                        print(f'Sorry, "{book.title}" is already checked out.')
                                        return
                                    print(f'Book title "{title}" not found in the library.')
                                    def return_book(self, title):
                                        for book in self._books:
                                            if book.title.lower() == title.lower():
                                                book.return_book()
                                                print(f'You have returned "{book.title}".')
                                                return
                                            print(f'Book titled "{title}" not found in the library.')
                                            def list_available_books(self):
                                                available_books = [book for book in self._books if book.is_available()]
                                                if available_books:
                                                    print("Available books:")
                                                    for book in available_books:
                                                        print(f' -"{book.title}" by {book.author}')
                                                    else:
                                                        print("No books are currently available.")
                                                        
        
                        
                    
                    

