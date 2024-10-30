# Description: This script tests various numeric conversion techniques
# Author: Symone Gant Newprogrammer

#Defined 
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

#Cast as integer
a_int = int(float(a.strip()))
b_int = int(b)
c_int = int(c.split()[0])
d_int = int(d.split()[1])

#Cast as Float 
a_float = float(a.strip())
b_float = float(b)
c_float = float(c.split()[0])
d_float = float(d.split()[1])

#Cast as float then integer
a_int_from_float = int(a_float)

#Use slicing to extract the numeric portion of the strings
a_numeric = int(a.strip().split()[0])
b_numeric = int(b)
c_numeric = int(c.split()[0])
d_numeric = int(d.split()[1])

#Use the .strip() method to remove leading/trailing spaces
a_stripped = a.strip()
d_stripped = d.strip()

# print the values and types of the new variables
print(f"a_int: {a_int}, type: {type(a_int)}")
print(f"b_int: {b_int}, type: {type(b_int)}")
print(f"c_int: {c_int}, type: {type(c_int)}")
print(f"d_int: {d_int}, type: {type(d_int)}")

print(f"a_float: {a_float}, type: {type(a_float)}")
print(f"b_float: {b_float}, type: {type(b_float)}")
print(f"c_float: {c_float}, type: {type(c_float)}")
print(f"d_float: {d_float}, type: {type(d_float)}")

print(f"a_int_from_float: {a_int_from_float}, type: {type(a_int_from_float)}")

print(f"a_numeric: {a_numeric}, type: {type(a_numeric)}")
print(f"b_numeric: {b_numeric}, type: {type(b_numeric)}")
print(f"c_numeric: {c_numeric}, type: {type(c_numeric)}")
print(f"d_numeric: {d_numeric}, type: {type(d_numeric)}")

print(f"a_stripped: {a_stripped}, type: {type(a_stripped)}")
print(f"d_stripped: {d_stripped}, type: {type(d_stripped)}")

# I used float(a.strip()) to convert the string a to a float after removing leading/trailing spaces.
#I used int(c.split()[0]) and int(d.split()[1]) to extract the numeric portion of the strings c and d, respectively.
#I used the .strip() method to remove leading/trailing spaces from a and d.