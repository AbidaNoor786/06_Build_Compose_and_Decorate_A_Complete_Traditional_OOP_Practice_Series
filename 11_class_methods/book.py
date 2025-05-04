class Book:
    total_books = 0  
    
    def __init__(self, title):  # <-- Fixed here
        self.title = title
        Book.increment_book_count() 
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  
    
    @classmethod
    def get_total_books(cls):
        print(f"Total books: {cls.total_books}")


book1 = Book("Quraan")
book2 = Book("Advanced Python")
Book.get_total_books()
