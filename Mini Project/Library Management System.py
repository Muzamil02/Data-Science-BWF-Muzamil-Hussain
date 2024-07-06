class Library:
    def __init__(self):
        self.books = {}  # Dictionary to store book details with book ID as the key

    def add_book(self, book_id, title, author):
        if book_id in self.books:
            print(f"Book ID {book_id} already exists.")
        else:
            self.books[book_id] = {'title': title, 'author': author, 'available': True}
            print(f"Book '{title}' added successfully.")

    def update_book(self, book_id, title=None, author=None):
        if book_id in self.books:
            if title:
                self.books[book_id]['title'] = title
            if author:
                self.books[book_id]['author'] = author
            print(f"Book ID {book_id} updated successfully.")
        else:
            print(f"Book ID {book_id} not found.")

    def remove_book(self, book_id):
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book ID {book_id} removed successfully.")
        else:
            print(f"Book ID {book_id} not found.")

    def borrow_book(self, book_id):
        if book_id in self.books:
            if self.books[book_id]['available']:
                self.books[book_id]['available'] = False
                print(f"Book ID {book_id} borrowed successfully.")
            else:
                print(f"Book ID {book_id} is currently not available.")
        else:
            print(f"Book ID {book_id} not found.")

    def return_book(self, book_id):
        if book_id in self.books:
            if not self.books[book_id]['available']:
                self.books[book_id]['available'] = True
                print(f"Book ID {book_id} returned successfully.")
            else:
                print(f"Book ID {book_id} was not borrowed.")
        else:
            print(f"Book ID {book_id} not found.")

    def search_books(self, title=None, author=None):
        results = []
        for book_id, details in self.books.items():
            if (title and title.lower() in details['title'].lower()) or (author and author.lower() in details['author'].lower()):
                results.append((book_id, details))
        if results:
            for book_id, details in results:
                print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Available: {details['available']}")
        else:
            print("No books found matching the criteria.")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book_id, details in self.books.items():
                print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Available: {details['available']}")


def main():
    library = Library()

    print("**************************************************")
    print("** Welcome to Our Library Management System **")
    print("**************************************************")

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Remove Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Search Books")
        print("7. Display All Books")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_id = input("Enter book ID: ")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            library.add_book(book_id, title, author)
        elif choice == '2':
            book_id = input("Enter book ID to update: ")
            title = input("Enter new title (leave blank to skip): ")
            author = input("Enter new author (leave blank to skip): ")
            library.update_book(book_id, title if title else None, author if author else None)
        elif choice == '3':
            book_id = input("Enter book ID to remove: ")
            library.remove_book(book_id)
        elif choice == '4':
            book_id = input("Enter book ID to borrow: ")
            library.borrow_book(book_id)
        elif choice == '5':
            book_id = input("Enter book ID to return: ")
            library.return_book(book_id)
        elif choice == '6':
            title = input("Enter title to search (leave blank to skip): ")
            author = input("Enter author to search (leave blank to skip): ")
            library.search_books(title if title else None, author if author else None)
        elif choice == '7':
            library.display_books()
        elif choice == '8':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()