from custom_classes import DVD, Book


def main():
    book = Book("1984", "George Orwell", 328)
    dvd = DVD("Inception", "Christopher Nolan", 148)

    print("--- Library ---")
    print(book)
    print(dvd)

    print("\n--- Checking out the DVD ---")
    print(dvd.checkout())
    print(dvd)

    print("\n--- Trying to check out the DVD again ---")
    print(dvd.checkout())

    print("\n--- Library ---")
    print(book)
    print(dvd)


if __name__ == "__main__":
    main()
