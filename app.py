import json

class MyLibrary:
    """Handles adding, removing, searching, and updating a personal book library."""

    def __init__(self):
        """Sets up the initial empty library and loads data if available."""
        self.books = []
        self.data_file = "my_books.json"
        self.load_books()

    def load_books(self):
        """Tries to load books from a file. If the file doesn't exist or is broken, starts fresh."""
        try:
            with open(self.data_file, "r") as f:
                self.books = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        """Writes the current list of books to a file so it's not lost."""
        with open(self.data_file, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self):
        """Takes book details from user and adds the book to the library."""
        title = input("Book title: ")
        author = input("Author name: ")
        year = input("Year published: ")
        genre = input("Genre of the book: ")
        has_read = input("Have you read it? (yes/no): ").strip().lower() == "yes"

        book = {
            "title": title,
            "author": author,
            "year": year,
            "genre": genre,
            "read": has_read
        }

        self.books.append(book)
        self.save_books()
        print("✅ Book added!\n")

    def remove_book(self):
        """Deletes a book from the library based on the title provided by the user."""
        title = input("Enter the title of the book to delete: ")

        found = False
        for b in self.books:
            if b["title"].lower() == title.lower():
                self.books.remove(b)
                found = True
                break

        if found:
            self.save_books()
            print("🗑️ Book deleted successfully.\n")
        else:
            print("⚠️ Book not found.\n")

    def search_books(self):
        """Lets user look for books by title or author."""
        print("Search by: ")
        print("1. Title")
        print("2. Author")
        choice = input("Choose (1 or 2): ")
        query = input("Enter your search: ").lower()

        matches = []
        for book in self.books:
            if (choice == "1" and query in book["title"].lower()) or \
               (choice == "2" and query in book["author"].lower()):
                matches.append(book)

        if matches:
            print("\n🔎 Search Results:")
            for i, b in enumerate(matches, 1):
                status = "Already Read" if b["read"] else "Unread"
                print(f"{i}. {b['title']} by {b['author']} ({b['year']}) - {b['genre']} - {status}")
            print()
        else:
            print("😕 No results found.\n")

    def edit_book(self):
        """User can update details of a book by providing its title."""
        title = input("Enter the book title to update: ")
        for book in self.books:
            if book["title"].lower() == title.lower():
                print("Leave input empty to keep current value.")
                new_title = input(f"New title ({book['title']}): ")
                new_author = input(f"New author ({book['author']}): ")
                new_year = input(f"New year ({book['year']}): ")
                new_genre = input(f"New genre ({book['genre']}): ")
                new_read = input("Have you read it? (yes/no): ").strip().lower()

                if new_title:
                    book["title"] = new_title
                if new_author:
                    book["author"] = new_author
                if new_year:
                    book["year"] = new_year
                if new_genre:
                    book["genre"] = new_genre
                if new_read in ["yes", "no"]:
                    book["read"] = new_read == "yes"

                self.save_books()
                print("✏️ Book info updated!\n")
                return

        print("⚠️ Book not found.\n")

    def display_books(self):
        """Shows all books stored in the library."""
        if not self.books:
            print("📭 No books in your library yet.\n")
            return

        print("\n📚 Your Book List:")
        for idx, book in enumerate(self.books, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        print()

    def reading_stats(self):
        """Shows how many books are read vs unread."""
        total = len(self.books)
        read_count = sum(1 for book in self.books if book["read"])
        progress = (read_count / total * 100) if total > 0 else 0
        print(f"\n📊 Total books: {total}")
        print(f"✅ Completed: {read_count}")
        print(f"📈 Progress: {progress:.1f}%\n")

    def run(self):
        """Runs the main menu loop for user to interact with."""
        while True:
            print("=== 📘 Personal Library Manager ===")
            print("1. Add book")
            print("2. Delete book")
            print("3. Search books")
            print("4. Update book")
            print("5. Show all books")
            print("6. View reading stats")
            print("7. Exit")
            choice = input("Choose an option (1-7): ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_books()
            elif choice == "4":
                self.edit_book()
            elif choice == "5":
                self.display_books()
            elif choice == "6":
                self.reading_stats()
            elif choice == "7":
                print("👋 Goodbye! Your books are saved.")
                break
            else:
                print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    app = MyLibrary()
    app.run()
