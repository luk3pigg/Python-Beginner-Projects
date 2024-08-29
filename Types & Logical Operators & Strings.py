#Python types

print(type("Hello World"))
print(type(4.72))
print(type(13))
print(type(True))

#moving to integers

print(4.72, int(4.72)) # Python rounds down
print(4.72, int(4.72), int(round(4.72)))

#Moving strings to integers
print("12345", int("12345"))
#But can't move strings to integers when there's letters invovled

#Moving to floats
print(float(18))

#Moving to strings
print(str(18))

#Logical Operators
#and, or, not

x = 6
print(x > 0 and x < 10)
#True

y = 23
print(not(y % 2 == 0 or y > 4 ))

#Strings

#Integers, floats, and booleans are simple data types - can't be broken down
#Lists, strings, can be broken down...into characters!

#Concatenation
greeting = "Hello"
name = " Luke"
print(greeting + name)
print(greeting, "everyone, and", name)
print("My shoe size is", greeting, "and my age is", name)

# * operator
print(greeting + name*3)

#Index operator
name = "Brad"
print(name[2]) # like lists, starts from 0
print(name[0] + name[3])
#slicing
print(name[0:2])
print(name[2:])
print(name.upper())

name = "ellie"
print(name.count("l"))
print(name.replace("l", "d", 2))
new_name = name.replace("l", "d")
print(new_name)
print(len(name))

#format strings
your_name = input("Your name: ")
hello = "Hello {}".format(your_name)
print(hello)
print(f"Hello {your_name}")

print("orange" < "strawberry")
print(ord("o")) # lowercase and uppercase letters have different numbers
print(chr(38))
#can perform maths on strings!

#in and not
fruit = "banana"
print("a" in fruit) # bools again
print("s" not in fruit)
x = "hello"
y =""
for character in x:
    y = character.upper() + y
print(y) # this produces OLLEH

x = "hello"
y =""
for character in x:
    y = character.upper() + y
print(y) # this produces OLLEH - do y = y + character.upper() to produce it in correct order
