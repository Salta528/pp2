class Str:
    def __init__(self):
        self.str=""
    def get_string(self):
        self.str=input()
    def print_string(self):
        print(self.str.upper())
str=Str()
str.get_string()
str.print_string()