# print("Hello world from my first script")


# def convert_mg_to_g(mg):
#     g = mg / 1000
#     print(g)
#     return g


# print(f"converted mass is: {convert_mg_to_g(2500)} g")


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def summary(self):
        print(f"Title: {self.title}")
        print(f"Pages: {self.pages}")

        if self.pages >= 300:
            print(f"Length: Long")
        else:
            print(f"Length: Short")


long_book = Book("Programming in Python", 3000)
short_book = Book("TL/DR: Programming in Python", 200)

long_book.summary()
short_book.summary()
