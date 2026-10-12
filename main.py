from custom_classes import DVD, Book, LibraryCollection, MediaItem


def main():
    library = LibraryCollection()

    book = Book("1984", "George Orwell", 328)
    dvd = DVD("Inception", "Christopher Nolan", 148)
    album = MediaItem("Abbey Road", "The Beatles")
    second_book = Book("Dune", "Frank Herbert", 412)

    print("--- Adding items to the library ---")
    for item in [book, dvd, album, second_book]:
        library.add_item(item)
        print(f"Added: {item}")

    print("\nAvailable titles:", library.list_available())

    print("\n--- Checking out 2 items ---")
    print(f"{book.title}: {book.checkout()}")
    print(f"{dvd.title}: {dvd.checkout()}")

    print("\nAvailable titles:", library.list_available())


if __name__ == "__main__":
    main()
