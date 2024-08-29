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

