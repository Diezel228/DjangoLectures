my_income= 100 #snake case for variables in python
tax_rate = 0.1

my_var = "whats up people"
my_list = [100,200,300,400,500]
#my_list = my_var#how can i set this to be each word?
print(my_list[1:4])
my_list.insert(3, my_var)
print(my_list)
print(my_list.append(my_var))#I thought this was weird
yea = my_list.pop#just google methods for list and other data types
print(yea)


my_taxes = tax_rate * my_income
print(my_taxes.hex())#the method must be finished with () cause its a function.
new_var = my_var[1:8]+"!"

print(F"{my_var}, my income is {my_income}. \nmy taxes are {my_taxes}, so {new_var}")#fstring sting interpolation


##dictionaries
my_dict = {"guest01":"Amy","guest02":"Donald","guest03":"Gusto"}
my_dict["guest04"] = "Sara"#adding new key/value pair
my_dict["guest02"] = "Mark"#updating value
print(my_dict)
#print(my_dict["guest01"])

stock_prices = {"GOOGL":[200,210,220],"GME":[20,100,300]}
history =stock_prices["GOOGL"]

print(f"fist day price is: {history[0]}")

#my_dict = my_dict["guest01"] = {"OUTER": {"INNER": 100}}
#print(mydict["OUTER"]["INNER"])
print(my_dict.values(), my_dict.items(), my_dict.keys())

#tuples are immutable :) less methods too than list yeahh!!!!! .items() returns key/value pairs
my_tuple = (1,2,3,4)
print(my_tuple)#think constants

#if elif else

password = "mypassword"
stored_pw = "mypassword"
admin = False 

if password == stored_pw and admin:#admin first is no fun
    print("pw match!")
elif admin:
    print("not granted")
else:
    print("no pw match")

for i in my_tuple:
    print("hello")

employees = {'ceo': 'cindy','cfo':'james'}
for position in employees:#naming iterations position
    print(f"the {position} is held by {employees[position]}")
    print(employees["ceo"])
    #1st:entering the key returns the values. 
    #2nd:We pass key back to dict as the param for employees returning value per key lol.
    #name each key position and for each position .......
    print(employees.items())

#tuple unpacking/////////////////////////////////////////////////
listy = [("a","b"),("c","d"),(1,2)]#list with tuples inside
for item1,item2 in listy:             #use when you know your list 
    print(item2)
    print(item1)



#while looops
blah = 0
while blah < 5:
    print(f"do ITITITITIITIT number: {blah}")
    blah = blah+1


#functions
def my_function(name,num1,num2): #snake casing is convention for python functions.
    '''
    the "Docstring" explains a function via help()
    '''
    print("hello " +name)#displays to "console"
    return num1+num2#can save to variable

new_var = my_function('daniel',2,54)#56(sum) will no be returned unless assigned to var
print(new_var)

datastream = [1,2,4,5,4,3,2,4,6,7,8,10,36,35,5]
def checker(list_to_check):
    for num in list_to_check:
        if num == 10:
            return True
        #return at last indent instead of else in this scope so it doesnt stop on 1st item.
    return False

print(checker(datastream))