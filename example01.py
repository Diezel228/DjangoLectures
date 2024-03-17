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