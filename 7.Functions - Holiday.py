# This program wil calculate a user's total holiday cost (plane cost, hotel cost and car-rental cost)

# Create a variable for the city the user will go to and check that it is a valid number.
while True:
  city_flight = input("Please select the city you will be flying to (Enter a number option (1 to 3):\n1. Barbados\n2. Oslo\n3. New York\n")

  if city_flight.isdigit() and int(city_flight) <=4:
    city_flight = int (city_flight)
    break
  else:
    print ("Invalid number provided. Please enter a number from the options provided")

# Create another variable for the name of the city to be used later
if city_flight == 1:
  city = "Barbados"
elif city_flight == 2:
  city = "Oslo"
else:
  city = "New York"

# Create a variable for the number of nights the user will be staying at a hotel.
while True:
  num_nights = input("Please enter the number of nights you will be staying at a hotel: ")

  if num_nights.isdigit():
    num_nights = int (num_nights)
    break
  else:
    print ("Invalid number provided. Please enter a valid number of nights")


# Create a variable for the number of rental days the user will be hiring a car for.
while True:
  rental_days = input("Please enter the number of days you will be hiring a car for: ")

  if rental_days.isdigit():
    rental_days = int (rental_days)
    break
  else:
    print ("Invalid number provided. Please enter a valid number of rental days")


# Define a function for the hotel cost and set the cost based on user input
def hotel_cost (num_nights):
  x = num_nights * 64
  return x

total_hotel_cost = hotel_cost (num_nights)



# Define a function for the plane cost and set the cost for each holiday option
def plane_cost (city_flight):
  if city_flight == 1:
    y = 550
  elif city_flight == 2:
    y = 200
  else:
    y = 375
  return y

total_plane_cost = plane_cost (city_flight)


# Define a function for car rental cost and set the cost based on user input
def car_rental (rental_days):
  z = rental_days * 27
  return z

total_car_rental = car_rental (rental_days)


# Define a function for the total holiday and set the total cost based on user input
def holiday_cost (hotel_cost, plane_cost, car_rental):
  t = total_hotel_cost + total_plane_cost + total_car_rental
  return t

total_cost_holiday = holiday_cost (hotel_cost, total_plane_cost, car_rental)


# print out the details of the holiday
print (f"The hotel cost in {city} is {total_hotel_cost}.")
print (f"The plane cost to {city} is {total_plane_cost}.")
print (f"The car rental cost in {city} is {total_car_rental}.")
print (f"The total cost of the holiday in {city} is {total_cost_holiday}.")