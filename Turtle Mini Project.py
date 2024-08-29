

#Turtle Mini Project
#Drawing package built into Python
import turtle 

turtle.bgcolor("black") #note the american spelling
turtle.pensize(2)
turtle.color("red")
turtle.speed(0)

# =============================================================================
# number_of_sides = int(input("How many sides would you like the regular polygon to be drawn to have?"))
# 
# if number_of_sides == 3:
#     for i in range(number_of_sides):
#         turtle.forward(50)
#         turtle.left(120)
#     turtle.done()
# elif number_of_sides == 4:
#     for i in range(number_of_sides):
#         turtle.forward(50)
#         turtle.left(90)
#     turtle.done()
# else:
#     print("Sorry, this shape is not currently supported in this drawing package")
#     
# 
# number_of_sides = int(input("How many sides would you like the regular polygon to be drawn to have?"))
# angle = 360/number_of_sides
# for i in range(number_of_sides):
#     turtle.forward(100)
#     turtle.left(angle)
# =============================================================================


# =============================================================================
# To comment out large blocks of code in Spyder, ctrl + 4
# =============================================================================

# =============================================================================
# turtle.speed(0)
# for colours in ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]:
#     turtle.color(colours)
#     turtle.circle(150)
#     turtle.left(60) # to make sure the circles don't overlap each other
# turtle.done()    
# =============================================================================

for i in range(6):
    for colours in ["red", "orange", "yellow", "green", "blue", "indigo"]:
        turtle.color(colours)
        turtle.circle(150)
        turtle.left(10) # to make sure the circles don't overlap each other
turtle.done()   


