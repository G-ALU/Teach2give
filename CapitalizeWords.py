'''Write a program that accepts a string as input, capitalizes the first letter of each word in the
string, and then returns the result string.
Examples:
"hi"=> returns "Hi"
"i love programming"=> returns "I Love Programming" '''

def capitalize_first(text):

  return text.title()

while True:
  try:

    text = input("Enter a string: ")
    # Capitalize and print the result
    capitalized_text = capitalize_first(text)
    print(capitalized_text)
    break  # Exit the loop after one iteration
  except ValueError:
    print("Invalid input. Please enter a string.")

