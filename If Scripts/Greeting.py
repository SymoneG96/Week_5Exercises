import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# Determine the appropriate greeting
if current_hour < 10:
    greeting = "Good morning!"
elif 10 <= current_hour < 17:  # 17 represents 5:00 PM
    greeting = "Good day!"
else:
    greeting = "Good evening!"

# Display the greeting
print(greeting)

import datetime

# Get the current hour
current_hour = datetime.datetime.now().hour

# Determine the appropriate greeting
if 11 <= current_hour <= 23 or 0 <= current_hour < 4:  # Between 11 PM and 4 AM
    greeting = "What are you doing up so late??"
elif current_hour < 10:
    greeting = "Good morning!"
elif 10 <= current_hour < 17:  # 17 represents 5:00 PM
    greeting = "Good day!"
else:
    greeting = "Good evening!"

# Display the greeting
print(greeting)