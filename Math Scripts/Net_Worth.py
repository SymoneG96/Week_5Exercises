# 1
total_assets = 250000
total_liabilities = 100000

net_worth = total_assets - total_liabilities

print(f"Your net worth is ${net_worth:.2f}")

# Steps 
# Assign the total assets and total liabilities to variables.
#Calculate the net worth by subtracting the liabilities from the assets.
#Use the print() function with an f-string to display the net worth, formatting it to 2 decimal places.

# 2 
length = 10
width = 5

area = length * width

print(f"The area of the rectangle is {area}")

#Assign the length and width of the rectangle to variables.
#Calculate the area by multiplying the length and width.
#Use the print() function with an f-string to display the area.

#3
bill_amount = 100
tip_percentage = 0.20

tip_amount = bill_amount * tip_percentage

print(f"The tip on a ${bill_amount} restaurant bill is ${tip_amount:.2f}")

#Steps Assign the bill amount and tip percentage to variables.
#Calculate the tip amount by multiplying the bill amount by the tip percentage.
#Use the print() function with an f-string to display the tip amount, formatting it to 2 decimal places.

#4
import math

radius = 5

area = math.pi * (radius ** 2)

print(f"The area of a circle with radius {radius} is {area:.2f}")

#Steps 
# Import the math module to access the pi constant.
#Assign the radius of the circle to a variable.
#Calculate the area using the formula and the math.pi constant.
#Use the print() function with an f-string to display the area, formatting it to 2 decimal places.

#5
initial_balance = 10000
interest_rate = 0.05  # 5% annual interest rate

years = 72 / (interest_rate * 100)
new_balance = initial_balance * 2

print(f"At a {interest_rate:.0%} interest rate, your savings account will be worth ${new_balance:,.2f} in {years:.1f} years")

#Steps 
#Assign the initial balance and interest rate (as a decimal) to variables.
#Calculate the number of years it takes to double the balance using the rule of 72 formula.
#Calculate the new balance by multiplying the initial balance by 2.
#Use the print() function with an f-string to display the results, formatting the interest rate as a percentage, the new balance with commas, and the number of years to 1 decimal place.