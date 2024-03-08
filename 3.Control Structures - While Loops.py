# This program asks the user to continue entering a number until -1 is input and then it will calculate an average of the numbers entered excluding the final -1 value used to break the while loop.

# First we initialise the variables total_inputs to calculate the sum of user inputs and count_inputs as the number of entered numbers
total_inputs = 0
count_inputs = 0

# Ask the user to input a number.
user_input = input("Please enter a number (-1 to exit): ")

# Use a try except block to check if the input is a valid number:
while True:
  try:
    number = int (user_input)
    break
  except ValueError:
    print ("Error: Please enter a valid number.")
    user_input = input("Please enter a number (-1 to exit): ")

user_input = int (user_input)

# Create a while loop to sum the total inputs and counts and calculate an average which is stored in a new variable average_inputs. We then print the average of the numbers. Another Try-Except block is used to check if subsequent values are numeric.
while user_input != -1 :
  total_inputs += user_input
  count_inputs += 1
  average_inputs = total_inputs / count_inputs

  user_input = input("Please enter another number (-1 to exit): ")

  while True:
    try:
      new_number = int (user_input)
      break
    except ValueError:
      print ("Error: Please enter a valid number.")
      user_input = input("Please enter another number (-1 to exit): ")

  user_input = int (user_input)

  if user_input == -1:
    print (f"the average of the {count_inputs} numbers input is {average_inputs}")
    break