# 1
fahrenheit = 77

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

#Steps 
#Assign the Fahrenheit temperature to a variable.
#Calculate the Celsius temperature using the formula.
#Use the print() function with an f-string to display the result, formatting the Celsius temperature to 2 decimal places.

#2 
celsius = 25

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

#Steps 
#Assign the Celsius temperature to a variable.
#Calculate the Fahrenheit temperature using the formula.
#Use the print() function with an f-string to display the result, formatting the Fahrenheit temperature to 2 decimal places.

#3
salary = 5000

tax_rate = 0.23
taxes_withheld = salary * tax_rate

print(f"With a salary of ${salary:.2f}, ${taxes_withheld:.2f} is withheld for taxes.")

#Steps 
#Assign the salary amount to a variable.
#Define the tax rate as a decimal (23% = 0.23).
#Calculate the taxes withheld by multiplying the salary by the tax rate.
#Use the print() function with an f-string to display the results, formatting the salary and taxes withheld to 2 decimal places.

#4
import math

# Example coordinates
x1 = 2
y1 = 3
x2 = 5
y2 = 7

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f}")

#Steps 
# Assign the x and y coordinates to variables.
#Import the math module to use the sqrt() function.
#Calculate the distance using the formula.
#Use the print() function with an f-string to display the result, formatting the distance to 2 decimal places.

#5 
length = 12
width = 15
tiles_per_box = 12
extra_tiles_percent = 0.1

total_area = length * width
total_tiles_needed = total_area
tiles_with_extra = total_tiles_needed * (1 + extra_tiles_percent)
boxes_needed = round(tiles_with_extra / tiles_per_box)

print(f"For a room {length}ft x {width}ft, you will need to buy {boxes_needed} boxes of tiles.")

#Steps 
#Assign the length, width, tiles per box, and extra tiles percentage to variables.
#Calculate the total area to be tiled.
#Calculate the total tiles needed, including the 10% extra.
#Divide the total tiles needed by the tiles per box and round up to get the number of boxes.

#6
num_people = 38
van_capacity = 15
van_rental_cost = 250

num_vans = (num_people + van_capacity - 1) // van_capacity
total_rental_cost = num_vans * van_rental_cost
cost_per_person = total_rental_cost / num_people

print(f"For {num_people} people, you will need {num_vans} vans.")
print(f"The total cost to rent the vans is ${total_rental_cost:.2f}")
print(f"The cost per person is ${cost_per_person:.2f}")

#Steps 
#Assign the number of people, van capacity, and van rental cost to variables.
#Calculate the number of vans needed by dividing the total number of people by the van capacity and rounding up.
#Calculate the total rental cost by multiplying the number of vans by the rental cost.
#Calculate the cost per person by dividing the total rental cost by the number of people.
#Use the print() function with f-strings to display the results.
