'''Write a program that takes an integer as input and returns true if the input is a power of two.
Examples:
8=> returns true
6=> returns false'''

def is_power_of_two(n):

  if n <= 0:
    return False
  # Efficiently check if n has only one set bit using bitwise AND with n-1
  return n & (n - 1) == 0

while True:
  try:
    num = int(input("Enter an integer: "))
    if is_power_of_two(num):
      print(f"{num} =>True.")
    else:
      print(f"{num} =>false.")
    break
  except ValueError:
    print("Invalid input. Please enter an integer.")

