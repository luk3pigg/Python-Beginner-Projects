#Functions take an argument, and produce a result
#General form: def function_name(argument):
    #####
    #return result
#x ^2 function
def squared(x):
    result = x**2
    return result

#recalling a function
print(squared(2))


def squared(x, y):
    result = x**2 + y**2
    return result
print(squared(2, 3))

#A new function
def born(country):
    return print(f"I am from {country}!")

born("England")

#A new function
def born(country):
    return print("I am from", country, "!")

born("England")  #This code has a space between the coutnry and the exclamation mark?

#A new function
def born(country):
    return print("I am from " + country + "!")

born("England") # this method uses string concatenation and is much better than the commas used above!

