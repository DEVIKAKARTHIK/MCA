class Publisher():
    def __init__(self,name):
        self.name=name
    def display(self):
        print(f"Name:{self.name}")
class Book(Publisher):
    def __init__(self,name,bookname,author):
        super().__init__(name)
        self.bookname=bookname
        self.author=author
    def display(self):
        super().display()
        print(f"Title={self.bookname}\t Author={self.author}")
b=Book(name="anan",bookname="kiitt",author="lasls")
b.display()      