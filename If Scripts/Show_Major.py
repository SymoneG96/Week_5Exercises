def get_major_info(major_code):
  """
  Retrieves the major name and department office location based on the major code.


    major_code: The major code.

  Returns:
    A tuple containing the major name and department office location.
  """
  if major_code == "BIOL":
    major_name = "Biology"
    department_office = "Science Bldg, Room 310"
  elif major_code == "CSCI":
    major_name = "Computer Science"
    department_office = "Sheppard Hall, Room 314"
  elif major_code == "ENG":
    major_name = "English"
    department_office = "Kerr Hall, Room 201"
  elif major_code == "HIST":
    major_name = "History"
    department_office = "Kerr Hall, Room 114"
  elif major_code == "MKT":
    major_name = "Marketing"
    department_office = "Westly Hall, Room 310"
  else:
    major_name = "Unknown Major"  # Alternative for unknown major codes
    department_office = None

  return major_name, department_office


# Tests
test_cases = [
    ("Craig Bowman", "ENG"),
    ("Bess Hambelton", "CSCI"),
    ("Charlie Brown", "BIOL"),
    ("Barack Obama", "HIST"),
    ("Eve Longoria", "MKT"),
    ("Freddy Kurger", "POLS")  # Made-up major code
]

for student_name, student_major in test_cases:
  major_name, department_office = get_major_info(student_major)
  print(f"Student Name: {student_name}")
  print(f"Major: {major_name}")
  if department_office:
    print(f"Department Office: {department_office}")
  print("-" * 20)