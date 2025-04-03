def add_numbers(x, y):
  """This function adds two numbers together."""
  sum = x + y
  return sum

def greet(name):
  """This function greets the person passed in as a parameter."""
  print(f"Hello, {name}!")

def is_even(number):
  """This function checks if a number is even."""
  if number % 2 == 0:
    return True
  else:
    return False

# Example usage
result = add_numbers(5, 3)
print(f"The sum is: {result}")

greet("Alice")

if is_even(10):
  print("10 is even")
else:
  print("10 is odd")

if is_even(7):
  print("7 is even")
else:
  print("7 is odd")
