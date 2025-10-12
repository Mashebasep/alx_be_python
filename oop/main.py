from book_class import Book
def main():
    my_book = Book("1984", "George Orwell", 1949)
    # Print method
    print(my_book.__str__())
    print(my_book.__repr__())
    del my_book
    

    
