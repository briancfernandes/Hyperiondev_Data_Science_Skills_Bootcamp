# This program will read a string and make each alterate character into an upper case and each other character into lower case.

# First we create the initial sentence and a variable to hold the final converted sentence.
sentence = "I hope that at the end of this course I will master Python!"
final_string = ""

# Create a for loop to go through the characters in the sentence to make the required conversion.
for i in range (len(sentence)):
  if i % 2 == 1:
    final_string += sentence [i].upper()
  else:
    final_string += sentence [i].lower() 

# Print the final sentence.
print (final_string)


# This next program will use the same sentence but make every alternative word lower and upper case.

# First we split the sentence into separate words.
words = sentence.split()

# Use a for loop to covert each alterate word into lower and upper case.
for w in range (0, len(words), 1):
  words [w] = words [w].lower()
for w in range (0, len(words), 2):
  words [w] = words [w].upper()

# Join the words back together and print the final sentence
final_sentence = " ".join(words)
print (final_sentence)

