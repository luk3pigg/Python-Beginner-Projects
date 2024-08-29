#Remember to ask chatGPT for solutions to all these after, too!
#Problem 1 - Assigning Variables
x = int(input("Choose your first number: "))
y = int(input("Choose your second number: "))
sum_ = x + y
minus = x - y
product = x*y
quotient = x/y

print("The sum of the numbers is", sum_ )
print("The difference between the numbers is", abs(minus))
print("The product of the numbers is", product )
print("The quotient of the numbers is", quotient )

#Solution given: can just print(x+y) straight away


#Problem 2 - List of all even numbers from 0 to 100
list_1 = list(range(0,101))
list_even = []
list_odd = []
for i in list_1:
    if i % 2 == 0:
        list_even.append(i)
    else:
        list_odd.append(i)
print(list_even)
print(list_odd)

print(list_even[0:10])
print(len(list_even))

#Solution given: much simpler way to list all the even numbers straight away:
list_2 = list(range(0,101,2))
print(list_2)

#Problem 3

num = int(input("Choose an integer of your choice"))
if num % 5 == 0:
    num = str(num)
    print("Your selected integer, " + num + ", is divisible by 5.")
else:
    num = str(num)
    print("Your selected integer, " + num + ", is not divisible by 5.")


#Problem 4

for i in range(6):
    print(i)

#Problem 5 - drawing a pentagon in turtle

import turtle 

turtle.bgcolor("black") #note the american spelling
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)

number_of_sides = int(input("How many sides would you like the regular polygon to be drawn to have?"))
angle = 360/number_of_sides
for i in range(number_of_sides):
    turtle.forward(100)
    turtle.left(angle)
turtle.done()

#Problem 6  - create function that tests whther three numbers are a Pythagorean Triple

# =============================================================================
# My original code:
# def pythagorean(x, y, z):
#     if x**2 + y**2 == z**2:
#         result = "Correct"   #can just do return print("....")instead for both if and else
#     else:
#         result = "Incorrect"
#     return print(result)
# x = 3
# y = 4
# z = 6
# print(pythagorean(x, y, z))
# =============================================================================

#Solution given:
def pythagorean_triple(a, b, c):
    if a**2 + b**2 == c**2:
        return True #boolean
    else:
        return False
    
print(pythagorean_triple(3, 4, 5))

#Problem 7 - spotting the error, while loops
n = 5
while n > 0:
    n = n - 1
    print(n)
    
#Problem 8 create two lists of 5 and plot against one another
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [12, 18, 23, 4, 89]
plt.plot(x, y, c="blue", linewidth=1, label="Line 1", linestyle="dashed", 
         marker='s', markerfacecolor="purple", markersize=10)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Two lines")
plt.legend()
plt.show()







    

    

