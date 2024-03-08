# This program enables the user to access two different financial calculators: an investment calculator and a home loan repayment calculator.

import math

# Print initial information for the user and ask for their choice of calculator selection.
print ("investment - to calculate the amount of interest you'll earn on your investment \nbond       - to calculate the amount you'll have to pay on a home loan \n" )
calculator = input ("Enter either 'investment' or 'bond' from the menu above to proceed: ")

# Ensure that all inputs of the calculator are valid by converting the input to lower case.
calculator = calculator.lower()

# Display an error message if a valid selection isn't made as the else message in the if statement.
# Calculation based on the investment calculator and whether simple or compound interest is selected.
if calculator == 'investment':
  deposit = int(input("Please enter the amount of money you are depositing: "))
  interest_rate = int(input("Please enter the interest rate (as a percentage without the % symbol): "))
  years = int(input("Please enter the number of years you plan to invest: "))
  interest = (input("Would you like the calculation to be done based on simple or compound interest? "))
  interest = interest.lower()

  if interest == 'simple':
    amount = int(deposit * (1 + ((interest_rate/100) * years)))
    print(f"the total amount at the end of the period (deposit + interest) is {amount}")

  elif interest == 'compound':
    amount = int(deposit * math.pow((1 + (interest_rate/100)), years))
    print(f"the total amount at the end of the period (deposit + interest) is {amount}")

  else:
    print("You have selected an incorrect option!")


# Calculation based on the bond calculator.
elif calculator == 'bond':
  house_price = int(input("Enter the present value of the house: "))
  interest_ratebond = int(input("Enter the interest rate (as a percentage without the % symbol): "))
  months = int(input("Enter the number of months expected to repay the bond: "))

  monthly_interest = (interest_ratebond/100)/12
  repayment = int((house_price * monthly_interest) / (1 - ((1 + monthly_interest)**(-months))))

  print (f"You will have to repay {repayment} each month")

# Response if any other input is made
else:
  print ("You have selected an incorrect option!")