class MediaItem:
    """A generic item in a library."""

    def __init__(self, title, author, is_available=True):
        self.title = title
        self.author = author
        self.is_available = is_available

    def checkout(self):
        if self.is_available:
            self.is_available = False
            return "Successful checkout"
        return "Already out"

    def return_item(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author} [{status}]"


class Book(MediaItem):
    """A book in the library."""

    def __init__(self, title, author, page_count, is_available=True):
        super().__init__(title, author, is_available)
        self.page_count = page_count

    def __str__(self):
        status = "Available" if self.is_available else "Checked Out"
        return f"{self.title} by {self.author}, {self.page_count} pages [{status}]"


class DVD(MediaItem):
    """A DVD in the library."""

    def __init__(self, title, author, duration, is_available=True):
        super().__init__(title, author, is_available)
        self.duration = duration

    def checkout(self):
        result = super().checkout()
        if result == "Successful checkout":
            print("Handle with care: Do not scratch the disc.")
        return result


class LibraryCollection:
    """A container that holds the library's media items."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_available(self):
        return [item.title for item in self.items if item.is_available]
