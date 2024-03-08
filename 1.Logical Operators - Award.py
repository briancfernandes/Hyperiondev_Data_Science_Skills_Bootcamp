# This programme determines the award a person competing in a triathlon will receive.

# Ask the user for the individual times for each event.
swim_time = int(input("Enter the swimming time in minutes: "))
cycling_time = int(input("Enter the cycling time in minutes: "))
running_time = int(input("Enter the running time in minutes: "))
total_time = swim_time + cycling_time + running_time

# Determine the awards based on the total time

if (total_time <= 100):
  print ("Provincial Colours awarded")
elif (total_time >= 101) and (total_time<= 105):
  print ("Provincial Half Colours awarded")
elif (total_time >= 106) and (total_time<= 110):
  print ("Provincial Scroll awarded")
else:
  print ("No award")