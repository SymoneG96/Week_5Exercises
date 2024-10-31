def calculate_gross_pay(pay_rate, hours_worked):
 
  if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
  else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
  return gross_pay


def calculate_annual_gross_pay(pay_rate, hours_worked_per_week):
 
  weekly_gross_pay = calculate_gross_pay(pay_rate, hours_worked_per_week)
  annual_gross_pay = weekly_gross_pay * 52  # Assuming 52 weeks in a year
  return annual_gross_pay


def calculate_federal_tax(annual_gross_income, filing_status):
  """
  Calculates federal tax based on annual income and filing status.

  Args:
    annual_gross_income: The annual gross income.
    filing_status: The filing status ('single' or 'joint').

  Returns:
    The calculated federal tax rate.
  """
  if filing_status == 'single':
    if annual_gross_income <= 10275:
      tax_rate = 0.10
    elif annual_gross_income <= 41775:
      tax_rate = 0.12
    elif annual_gross_income <= 89075:
      tax_rate = 0.22
    elif annual_gross_income <= 170050:
      tax_rate = 0.24
    elif annual_gross_income <= 215950:
      tax_rate = 0.32
    elif annual_gross_income <= 539900:
      tax_rate = 0.35
    else:
      tax_rate = 0.37
  elif filing_status == 'joint':
    if annual_gross_income <= 20550:
      tax_rate = 0.10
    elif annual_gross_income <= 83550:
      tax_rate = 0.12
    elif annual_gross_income <= 178150:
      tax_rate = 0.22
    elif annual_gross_income <= 340100:
      tax_rate = 0.24
    elif annual_gross_income <= 431900:
      tax_rate = 0.32
    elif annual_gross_income <= 647850:
      tax_rate = 0.35
    else:
      tax_rate = 0.37
  else:
    raise ValueError("Invalid filing status. Must be 'single' or 'joint'.")

  return tax_rate

# Example
pay_rate = 75.00
hours_worked_per_week = 40
filing_status = 'single'

annual_gross_income = calculate_annual_gross_pay(pay_rate, hours_worked_per_week)
weekly_gross_pay = calculate_gross_pay(pay_rate, hours_worked_per_week)
tax_rate = calculate_federal_tax(annual_gross_income, filing_status)
tax_withholding = weekly_gross_pay * tax_rate
net_pay = weekly_gross_pay - tax_withholding

print(f"You worked {hours_worked_per_week} hours this period.")
print(f"Because you earn ${pay_rate:.2f} per hour, your gross weekly pay is ${weekly_gross_pay:.2f}")
print(f"Your filing status is {filing_status}")
print(f"Your tax withholding for the week is ${tax_withholding:.2f}")
print(f"Your net pay is ${net_pay:.2f}") 