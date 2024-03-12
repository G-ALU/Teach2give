# Write a program that counts the number of vowels in a sentence. eg " Hello World " => returns 2


def count_unique_vowels(sentence):

  vowels = set('aeiouAEIOU')
  unique_vowels = set()

  for char in sentence:
    if char in vowels:
      unique_vowels.add(char)  # Add unique vowels to the set

  vowel_count = len(unique_vowels)
  return vowel_count

sentence = input("Enter a sentence: ")

# Count unique vowels and print result
vowel_count = count_unique_vowels(sentence)
print(f"The sentence '{sentence}' has {vowel_count} vowels.")
