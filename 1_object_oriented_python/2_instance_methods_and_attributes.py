class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'This is a secret attribute.'

    def get_price(self):
        return (self.price - (self.price * self._discount)
                if hasattr(self, '_discount')
                else self.price)

    def set_discount(self, amount):
        self._discount = amount


b1 = Book('Brave New World', 'Leo Tolstoy', 1225, 39.95)
b2 = Book('War and Peace', 'JD Salinger', 234, 29.95)

print(b1.get_price())
print(b2.__secret)  # Gives an error due to the use of double underscores
