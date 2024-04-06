class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_info(self):
        self.title=input()
        self.author=input()
        print(self.title)
        print(self.author)
p1=Book("asd","asddf")
p1.display_info()