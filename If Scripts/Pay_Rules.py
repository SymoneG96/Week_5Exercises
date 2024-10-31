def calculate_gross_pay(pay_rate, hours_worked):
  """
  Calculates gross pay, including overtime if applicable.

  Args:
    pay_rate: The hourly pay rate.
    hours_worked: The number of hours worked.

  Returns:
    The calculated gross pay.
  """
  if hours_worked <= 40:
    gross_pay = pay_rate * hours_worked
  else:
    regular_pay = pay_rate * 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
    gross_pay = regular_pay + overtime_pay
  return gross_pay

test_cases = [
    (12.50, 20),   # Under 40 hours
    (25.50, 40),   # Exactly 40 hours
    (17.30, 45)    # Over 40 hours
]

for pay_rate, hours_worked in test_cases:
  gross_pay = calculate_gross_pay(pay_rate, hours_worked)
  print(f"Pay Rate: ${pay_rate:.2f}, Hours Worked: {hours_worked}, Gross Pay: ${gross_pay:.2f}")