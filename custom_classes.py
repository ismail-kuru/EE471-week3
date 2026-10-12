class MediaItem:
    """A generic item in a library that can be checked out and returned.

    Attributes:
        title: The title of the item.
        author: The author, director or artist of the item.
        is_available: True if the item is on the shelf, False if checked out.
    """

    def __init__(self, title, author, is_available=True):
        """Create an item with a title, an author and an availability status."""
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        """Check the item out if it is available.

        Returns:
            "Successful checkout" if the item was available, otherwise "Already out".
        """
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        return "Already out"

    def return_item(self):
        """Mark the item as available again."""
        self.is_available = True

    @property
    def status(self):
        """Return "Available" or "Checked Out" based on is_available."""
        return "Available" if self.is_available else "Checked Out"

    def __str__(self):
        """Return the item as "Title by Author [Available/Checked Out]"."""
        return f"{self.title} by {self.author} [{self.status}]"


class Book(MediaItem):
    """A book, which also knows how many pages it has.

    Attributes:
        page_count: The number of pages in the book.
    """

    def __init__(self, title, author, page_count, is_available=True):
        """Create a book with a title, an author and a page count."""
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        """Return the book as "Title by Author, N pages [Available/Checked Out]"."""
        return f"{self.title} by {self.author}, {self.page_count} pages [{self.status}]"


class DVD(MediaItem):
    """A DVD, which is fragile and needs a care reminder on checkout.

    Attributes:
        duration_minutes: The running time of the DVD in minutes.
    """

    def __init__(self, title, author, duration_minutes, is_available=True):
        """Create a DVD with a title, an author and a duration in minutes."""
        super().__init__(title, author, is_available)
        self.duration_minutes = duration_minutes

    def checkout(self):
        """Check the DVD out and print a care reminder if it succeeded.

        Returns:
            The same message as MediaItem.checkout().
        """
        result = super().checkout()
        # is_available is False both after a success and when already out,
        # so only the returned message tells us whether this checkout worked.
        if result == "Successful checkout":
            print("Handle with care: Do not scratch the disc.")
        return result


class LibraryCollection:
    """A container that holds the library's media items.

    Attributes:
        items: The MediaItem objects (or subclasses) in the collection.
    """

    def __init__(self):
        """Create an empty collection."""
        self.items = []

    def add_item(self, item):
        """Add a MediaItem, Book or DVD to the collection."""
        self.items.append(item)

    def list_available(self):
        """Return the titles of all items that are currently available."""
        return [item.title for item in self.items if item.is_available]
