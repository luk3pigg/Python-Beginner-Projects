#Tuples - similar to lists, but can't modify the elements within them
fruit = ("Apples", 4, "Bananas", 5, "Oranges", 6)
print(type(fruit))

list_of_fruit = ["Apples", 4, "Bananas", 5, "Oranges", 6]
print(type(list_of_fruit))

list_of_fruit[0] = "Strawberries" # replaces apples with strawbeeries
print(list_of_fruit)

fruit[0:3] # can still slice tuples...just can't modify their values
#what are the advantages of tuples over lists then?

#concatenation
fruit = fruit[:4] + ("Cherries", 10)
print(fruit)

#Tuples with 1 element must have a comma to be classed as a tuple
x = (5, )

#length if a tuple
print(len(fruit))

#Creating tuples
another_tuple = tuple(("Hello", 18, True)) # Must have a double bracket!!

#Converting tuples and lists

fruit = list(fruit)
fruit.append("Pears")
fruit = tuple(fruit)
print(fruit)
print(type(fruit))

#Unpacking tuples
fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, three, four, five) = fruit
print(one) # must have same number of elements

fruit = ("Apples", "Bananas", "Pears", "Oranges", "Strawberries")
(one, two, *three) = fruit # element with asterisk gets assigned to the appropiate amount of elements from original tuple
print(tuple(three))

#incorporate loops

for i in range(len(fruit)): # use len if you don't know the length of the tuple
    print(fruit[i])

#both lists and tuples can be unpacked

nested_list = [1, [2, 3], 4]
x, (y, z), w = nested_list

print(x)  # Output: 1
print(y)  # Output: 2
print(z)  # Output: 3
print(w)  # Output: 4

