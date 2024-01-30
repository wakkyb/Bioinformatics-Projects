def plane_ride_cost(city):
  """
  Calculates the cost of a plane ride to a given city.

  Args:
    city: The city to fly to.

  Returns:
    The cost of the plane ride.
  """

  prices = {
    "Charlotte": 183,
    "Tampa": 220,
    "Pittsburgh": 222,
    "Los Angeles": 475,
  }

  if city not in prices:
    return "Invalid city"

  return prices[city]

def capitalize_first_letter(string):
  """
  Capitalizes the first letter of a string.

  Args:
    string: The string to capitalize.

  Returns:
    The capitalized string.
  """

  first_letter = string[0].upper()
  rest_of_string = string[1:]
  capitalized_string = first_letter + rest_of_string

  return capitalized_string

total_cost = 0
while True:

  city = input("Enter the city name: ")
  city = capitalize_first_letter(city)
  cost = plane_ride_cost(city)
  print(cost)
  answer = input("Do you want to continue? (y/n): ")
  if answer == "n":
    break

