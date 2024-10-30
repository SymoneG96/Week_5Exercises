# Define the dictionary

person_info = {
    "name": "Kamille Gant",
    "address": "123 love St",
    "city": "San Diego",
    "state": "CA",
    "zip": "62576"
}

# Print the address as properly formatted for mailing
print(f"""
{person_info["name"]}
{person_info["address"]}
{person_info["city"]}, {person_info["state"]} {person_info["zip"]}
""")

# Remove the key:value pair for name
del person_info["name"]

# Add a new variable for full_name as a tuple
full_name = ("Kamille", "Gant")

# Use the .update() method to add a new key:value pair
person_info.update({"honorific": "Mrs."})


# Print the formatted address again, updating as needed
print(f"""
{person_info.get("honorific", "")} {full_name[0]} {full_name[1]}
{person_info["address"]}
{person_info["city"]}, {person_info["state"]} {person_info["zip"]}
""")

#In the first step, I define a dictionary called person_info with keys for name, address, city, state, and zip. I assign sample values to each of these keys.

#Next, I use a multi-line f-string (with triple quotes) to print the address in a properly formatted mailing format. This f-string pulls the values directly from my person_info dictionary.

#In the third step, I remove the name key-value pair from the person_info dictionary using the del statement.

#Then, I create a new variable called full_name as a tuple, and I store a first name and last name in it.

#In the fifth step, I use the .update() method to add a new key-value pair, 'honorific': 'Mrs.', to my person_info dictionary.

#Finally, I print the formatted address again. This time, I include the new honorific and full_name information. I use the .get() method to safely retrieve the honorific value, just in case it's not present in the dictionary.