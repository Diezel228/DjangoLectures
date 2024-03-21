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
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa


stu1 = Student(name="daniel",gpa="3.9!!!!")
stu2 = Student(name="yaya",gpa="3.8!!!!")
print(f"student results: \n\t{stu1.name,stu1.gpa}\n\t{stu2.name,stu2.gpa}")#you can't call the var name as a key(returns memory location), your calling the class and its methods!!