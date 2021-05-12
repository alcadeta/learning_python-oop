# BASIC CLASS DEFINITIONS

# Create a basic class.
class Book:
    def __init__(self, title):
        self.title = title


# Create instances of the class.
b1 = Book('Brave New World')
b2 = Book('War and Peace')

# Print the class and its properties.
print(b1)
print(b1.title)
