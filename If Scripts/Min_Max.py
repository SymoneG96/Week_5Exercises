def find_smallest_and_largest(a, b, c):
  """
  Finds and displays the smallest and largest of three numbers.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.
  """

  # Find the smallest
  smallest = a
  if b < smallest:
    smallest = b
  if c < smallest:
    smallest = c

  # Find the largest
  largest = a
  if b > largest:
    largest = b
  if c > largest:
    largest = c

  print(f"The smallest number is: {smallest}")
  print(f"The largest number is: {largest}")


# Tests
test_cases = [
    (789, 5, 200),
    (507, 102, 20),
    (209, 10, 77),
    (-10, 10, 100),
    (-5, 10, 0)
]

for a, b, c in test_cases:
  print(f"Numbers: {a}, {b}, {c}")
  find_smallest_and_largest(a, b, c)
  print("-" * 20)