class Book:
    def __init__(self,book_id, title, author, is_available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        if isinstance(is_available, str):
            self.is_available=is_available=='True'
        else:
            self.is_available=is_available
    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"{self.book_id} {self.title} {self.author} by {self.is_available}-{status}"
    def to_csv_format(self):
        return f"{self.book_id}, {self.title}, {self.author}, {self.is_available}\n"