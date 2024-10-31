# Set initial variables
bank_balance = 1200
savings_goal = 4000
weekly_savings = 300

# Calculate halfway point and 75% threshold
halfway_point = savings_goal / 2
seventy_five_percent_goal = savings_goal * 0.75

# While loop for weekly savings
while bank_balance < savings_goal:
  bank_balance += weekly_savings  # Add weekly savings to the balance

  # Additional logic for milestones
  if bank_balance >= seventy_five_percent_goal:
    treat_cost = 25  # Cost of the treat
    bank_balance -= treat_cost  # Deduct the treat cost
    print(f"So close! After treating myself, my balance is up to ${bank_balance:.2f}.")
  elif bank_balance >= halfway_point:
    print(f"Almost there! This week my balance is up to ${bank_balance:.2f}.")
  else:
    print(f"This week my balance increased to ${bank_balance:.2f}.")

# Goal reached
print(f"Goal met! My current balance is ${bank_balance:.2f}.")