from custom_classes import MediaItem


def main():
    book = MediaItem("1984", "George Orwell")
    movie = MediaItem("Inception", "Christopher Nolan")

    print("--- Library ---")
    print(book)
    print(movie)

    print("\n--- Checking out the book ---")
    print(book.checkout())
    print(book)

    print("\n--- Trying to check out the book again ---")
    print(book.checkout())

    print("\n--- Library ---")
    print(book)
    print(movie)


if __name__ == "__main__":
    main()
