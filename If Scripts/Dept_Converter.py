def get_department_name(department_code):
  """
  Determines the department name based on the department code.

  Args:
    department_code: The department code.

  Returns:
    The department name, or "Unknown" if the code is not found.
  """
  if department_code == 1:
    return "Marketing"
  elif department_code == 5:
    return "Human Resources"
  elif department_code == 10:
    return "Accounting"
  elif department_code == 12:
    return "Legal"
  elif department_code == 18:
    return "IT"
  elif department_code == 20:
    return "Customer Relations"
  else:
    return "Unknown"


# Test cases
test_codes = [1, 5, 10, 12, 18, 20, 30]  # 30 is an invalid code

for code in test_codes:
  department_name = get_department_name(code)
  print(f"Department Code: {code}, Department Name: {department_name}")