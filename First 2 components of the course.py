# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 11:20:27 2024

@author: luk3p
"""

#Code of the Future stuff

from math import sqrt
from math import factorial
number = 9
print(sqrt(number))

print(factorial(5))

#comments work like this - use hash tags

#Lists - make sure variable names are specific

my_list1 = [1, 2, 3, 4, 5, 6]   #eg 6 individuals, one owns 1 pair of shoes, 2,3...
my_list2 = list(range(1,101))  # takes list of numbers from number given to final number -1
print(my_list1)
print(my_list2)
my_list3 = list(range(1,101,10))  #3rd argument gives increments
print(my_list3)
type(my_list3)
#Range function only works with integers, not floats!

#Operations on Lists

my_list3[3] #gives the nth+1 element of a list - 0 is 1!
my_list3[-1]  #returns elements starting from the last element = -1 is the last element
#Slicing - use colon, not comma!
my_list3[1:]# if no number put after colon it just assumes the final value

len(my_list3)

#Maximum and minimum values of a list

max(my_list3)

min(my_list3)

#Add an element to end of a list

my_list3.append(120)
my_list3

#Reverse a list

my_list3.reverse()
my_list3

#Add two lists together - joins them, not addition

my_list1 + my_list3

#loops

#Create a list
my_list = [5, 8, 10, 12]
#Let's add 5 to each eleemnt in tbe list
#for loop
for element in my_list: #colon at end if loop
    element = element + 5
    print(element)  #prints vertically, line after line

# If Loop, and f-strings
a = 30
if a % 2 == 0:  #% is MOD function - remainder
    print(f"{a} is divisible by 2")
else:
    print(f"{a} isn't divisible by 2")
    
###############
#Cool Python Project - weighted exam score average

number_of_exams = int(input("Enter number of exams: ")) #Input must be an integer otherwise error message will be returned

total_credits = int(input("Enter how many credits these exams cover: "))

#begin with average of 0, then add up percentages from each exam
average = 0
for exam in range(number_of_exams):
    score = int(input("Enter exam score, as a percentage: "))
    exam_credits = int(input("Enter how many credits this exam was worth: "))
    average = average + score*exam_credits/total_credits
print("Your average is", average)
print(f"Your average is {average}")  # both of these methods are valid



    
    






