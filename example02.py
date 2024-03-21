#advanced python

#############################error handling & exceptions

try:
    print(10+"22")
except:
    print("error!")
finally:#do regardless
    print("woah")






#dvrything is an object!!!!
num =10.3
print(type(num))

#define your onw objects 
class Sample():
    #pass#pass does nothing
    def __init__(self,name):#this is definatly main function
        self.name = name

x = Sample(name="blueueueueuajs")#class now has an atttribute
print(type(x))# prints that i just made .Sample
print(x.name)

#class example number 2
class Student():

    planet="Earth" #CLASS OBJECT ATTRIBUTE(does not need self.) self sets stuff inside the functions to global!
    def __init__(self,name,gpa):
        self.name = name #ATTRIBUTE
        self.gpa = gpa


stu1 = Student(name="daniel",gpa="3.9!!!!")
stu2 = Student(name="yaya",gpa="3.8!!!!")
print(f"student results: \n\t{stu1.name,stu1.gpa}\n\t{stu2.name,stu2.gpa}")#you can't call the var name as a key(returns memory location), your calling the class and its methods!!
print(Student.planet)#we dont have to define planet 

class Agent():
    origin = "USA"

    def __init__(self,name,height,weight):#defining the attributes of an object!!! 
        self.name =name
        self.height = height
        self.weight = weight
x = Agent("Danni","6'",170)
x.weight = 160#you can change them butt:) whats the point I guess
print(x.weight)    


#another exxx to the s example!!!! ok kayne.
class Circle():
    pi = 3.14
    def __init__(self,radius):#most get this
        self.radius = radius
    def area(self):
        return self.radius*self.radius*Circle.pi #circle and self work the same like console or log
    def perimeter(self):
        return 2 * self.radius * self.pi
mycircle = Circle(radius=5)
print(mycircle.radius)
print(mycircle.area)
print(mycircle.area())#now it returns our result
print(mycircle.perimeter())



#silly method