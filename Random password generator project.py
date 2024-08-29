#Random password generator

from random import randint

#All uppercase password

password ="" # password starts as an empty string
length = int(input("How many characters would you like your password to be")) # have to mkae sure this input is stored as an integer otherwise there will be an error
for i in range(length):
    i = chr(randint(65,90)) # uppercase ABC....could make into lower using.lower() if wanted to
    password = str(password) + i #must be casted to a string
print(password)

# Upper and Lowercase password
password =""
for i in range(5):
    i = chr(randint(65,90))
    for j in range(5):   # nested for loop...not actaully necessary though, see below!
        j = chr(randint(65,90)).lower()
    password = str(password) + i + j
print(password)

#how to randomly decide whether a letter will be upper or lower case?? Would need to randomly decide whether to be uppercase or lowercase - random bool?

# Upper and Lowercase password
password =""
for i in range(5):
    i = chr(randint(65,90))
    j = chr(randint(65,90)).lower()
    password = str(password) + i + j
print(password)

#Adding numbers to the password:
    
# Upper and Lowercase password
password =""
for i in range(5):
    i = chr(randint(65,90))
    j = chr(randint(65,90)).lower()
    k = randint(0,10)
    password = str(password) + i + j + str(k)
print(password)


# Upper and Lowercase password - but 50 characters this time!
password =""
for i in range(5):
    i = chr(randint(65,90))
    for j in range(5):   
        j = chr(randint(65,90)).lower()
        password = str(password) + i + j   #this is indented inside the inner loop 
print(password)
#50 characters: outer loop 5 times, inner loop 5 times for each capital letter (i), inner loop adds on a pair of characters each time





#Another method:

password = ""
for i in range(10):
    if i % 2 == 0:
        i = chr(randint(65, 90))  # Uppercase letter
    else:
        i = chr(randint(65, 90)).lower()  # Lowercase letter
    password = password + str(i)  # Append to password. Changing round password and str affects wther password starts with capital or not

print(password)






