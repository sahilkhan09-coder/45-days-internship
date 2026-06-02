class LibraryItem:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def describe(self):
        return f"'{self.title}' by {self.author} ({self.year})"


class Book(LibraryItem):
    def __init__(self, title, author, year, pages):
        super().__init__(title, author, year)
        self.pages = pages

    def describe(self):
        return f"Book: '{self.title}' by {self.author} ({self.year}) - {self.pages} pages"


class EBook(LibraryItem):
    def __init__(self, title, author, year, file_size_mb):
        super().__init__(title, author, year)
        self.file_size_mb = file_size_mb

    def describe(self):
        return f"EBook: '{self.title}' by {self.author} ({self.year}) - {self.file_size_mb} MB"


book1 = Book("Python Basics", "John Smith", 2022, 250)
book2 = Book("Data Science Guide", "Alice Brown", 2023, 400)

ebook1 = EBook("AI Essentials", "Robert Lee", 2024, 15.5)
ebook2 = EBook("Machine Learning", "Emma Davis", 2021, 8.2)


library_items = [book1, book2, ebook1, ebook2]

for item in library_items:
    print(item.describe())


# isinstance()
print(isinstance(book1, LibraryItem))

# Explanation:
# This prints True because Book inherits from LibraryItem.
# Therefore, every Book object is also considered a LibraryItem object.
