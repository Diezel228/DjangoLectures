#advanced python

#############################error handling & exceptions(try except)

try:
    print(10+'22')#change data types
except IOError:
    print("You have an input/output error")
    print("Did you check the file permissions?")
except TypeError:
    print("You are using the wrong data types!")
except:
    print("you got error")
else:
    print("ELSE BLOCK RAN")

finally:
    print("will run regardless of error")


"""OOP//////////////////////

class NameOfClass():#camelcase
    def __init__(self,param1,param2) -> None:  #i think this is like the main() in c#
        self.param1=param1
        self.param2=param2
    def some_method(self):
        #perfome action
        print("self.param1")

"""
#creating a class "Sample"
class Sample():#you dont always need the ()
    pass
num = Sample()
print(type(num))