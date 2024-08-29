# =============================================================================
# #Booleans - 2 constants, True or False.
# print(type(True))
# print(type("True"))
# #Both return the word True on the screen, but one is a string and one is Boolean
# print(5 == 6)
# print(5 < 6)
# =============================================================================
#Incorporating the if statement with a boolean
x = 11
y = 5
if x % y == 0: # % is modulus, remainder function in Python
    print(True)
else:
    print(False)

# while loop

number = 1
while number < 4:
    print(number)
    if number == 3:
        break     # Alternatives are 'continue', 'return'... 
    number = number + 1

        
number = 2
while number < 4:
    print(number)
    number = number + 1
else:
    print("number is no longer less than 4")
   
#If statements
number = int(input("choose an integer"))
if number > 0:
    print("Positive number")
elif number == 0:
    print("Zero")
else:
    print("Negative number")
