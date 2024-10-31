# Description: This script tests various numeric conversion techniques
# Author: Symone Gant Newprogrammer

#Defined 
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a_stripped = a.strip()          # Remove whitespace
a_float = float(a_stripped)     # Convert to float
a_int = int(a_float)           # Convert to integer

b_int = int(b)                 # Convert to integer
b_float = float(b)             # Convert to float

c_split = c.split()            # Split into list
c_first = c_split[0]           # Get first element
c_first_int = int(c_first)     # Convert first element to integer

c_split = c.split()            # Split into list
c_first = c_split[0]           # Get first element
c_first_int = int(c_first)     # Convert first element to integer

d_stripped = d.strip()         # Remove whitespace
d_split = d_stripped.split()   # Split into list
d_number = d_split[1]          # Get the number
d_int = int(d_number)          # Convert to integer

#Printed 

# Original variable a = " 101.1 "
print("a_stripped:", a_stripped)      # "101.1"
print("a_float:", a_float)           # 101.1
print("a_int:", a_int)               # 101

# Original variable b = '55'
print("b_int:", b_int)               # 55
print("b_float:", b_float)           # 55.0

# Original variable c = "402 Stevens"
print("c_split:", c_split)           # ['402', 'Stevens']
print("c_first:", c_first)           # "402"
print("c_first_int:", c_first_int)   # 402

# Original variable d = 'Number 5 '
print("d_stripped:", d_stripped)      # "Number 5"
print("d_split:", d_split)           # ['Number', '5']
print("d_number:", d_number)          # "5"
print("d_int:", d_int)               # 5

#Stripping removes extra whitespace
#Converting to float adds a decimal point
#Converting to int removes any decimal places
#Splitting creates a list from space-separated strings
#Accessing list elements lets me work with specific parts of the split string