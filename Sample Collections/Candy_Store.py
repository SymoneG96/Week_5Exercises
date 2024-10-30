
# Step 1: Create two tuples
candy_types = ("Chocolate Bar", "Gummy Bears", "Lollipop")
fruit_flavors = ("Strawberry", "Mango", "Lemon")

# Step 2: Create a set of candy combinations
candy_combinations = set()
for candy in candy_types:
    for flavor in fruit_flavors:
        candy_combinations.add(f"{candy} ({flavor})")

# Step 3: Create the output message and print the set
print("Today's candy options include:")
print(candy_combinations)

# Step 4: Print the output multiple times
print("\nToday's candy options include:")
print(candy_combinations)
print("\nToday's candy options include:")
print(candy_combinations)

#Steps create two tuples: candy_types and fruit_flavors, each containing 3 elements.
#Create a new set called candy_combinations. I used nested loops to iterate through the candy_types and fruit_flavors tuples, and for each combination, we create a string and add it to the set.
#Printed the contents of the candy_combinations set.
#Printed the contents of the candy_combinations set multiple times.