#Write a program to generate the Fibonacci sequence up to 100.

def fibonacci(n):

  a, b = 0, 1
  for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

fibonacci(100)
