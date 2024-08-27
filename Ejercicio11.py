while True:
  user_input = input("Insert your birth year: ")
  current_year = input("Insert the current year: ")
 

  if len(user_input) == 4 and len(current_year):
    user_input = int(user_input)
    current_year = int(current_year)
    Age = current_year - user_input
    print("Your age is: ", Age)
    break
  else:
    print("Invalid input. Number should be at least 4 digits")