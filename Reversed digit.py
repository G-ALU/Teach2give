'''Write a program that takes an integer as input and returns an integer with reversed digit
ordering.
Examples:
For input 500, the program should return 5.
For input -56, the program should return -65.
For input -90, the program should return -9.
For input 91, the program should return 19 '''


def reverse_integer(num):


  # Handle negative numbers separately
  is_negative = num < 0
  num = abs(num)  # Convert to positive for processing

  reversed_num = 0
  while num > 0:
    # Extract the last digit
    digit = num % 10
    # Add the digit to the reversed number (considering overflow)
    if reversed_num > (2**31 - 1) // 10 or (reversed_num == (2**31 - 1) // 10 and digit > 7):
      return 0

    reversed_num = reversed_num * 10 + digit
    # Remove the last digit from the original number
    num //= 10

  # Return the reversed number with the original sign
  return -reversed_num if is_negative else reversed_num

while True:
  try:
    # Get user input as an integer
    num = int(input("Enter an integer: "))
    # Reverse and print the result
    reversed_int = reverse_integer(num)
    if reversed_int == 0:
      print("Error: Input caused integer overflow.")
    else:
      print(f"Reversed integer: {reversed_int}")
    break  # Exit the loop after one iteration
  except ValueError:
    print("Invalid input. Please enter an integer.")

