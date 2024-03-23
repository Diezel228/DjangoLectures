#also modules :)
from python.mymodule import useful_func #import from and call on line:26 ()
from python.mymodule import UsefullClass #followed by making an instance of the class
my_instance = UsefullClass("HEllo")


#dunder methods EX: __init__
#how does python know what a user defined class or object should actually print?


#dunder methods methods linked to built-in functions or special calls
class Book():
    def __init__(self,title,author,pages) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        return f"{self.title} wirtten by {self.author}\t{self.pages}"
    
    def __len__(self):
        return 99

mybook = Book("Python ROcks!","daniel lol",120)
print(mybook)#returns the memoryspace the varaible is stored at 
print(len(mybook)) 
useful_func()
#remember print(my_instance) will display mem location. 
my_instance.report()
        