# Define the asterisk in the variable stars and create an index variable for iterations of the number of stars
stars = "*"
index = 9

# Create a for loop for the number of stars with an if statement which has 2 parts:
# For the increasing number of stars to 5 we increase the number of stars per iteration
# For the decreasing number of stars after 5 we use the index variable to display the number
for i in range(0,index):
  if i < 5: 
    print(stars)
    stars = stars +"*"
  
  else:
    index = 9 - i
    print(stars[0:index])
 
  