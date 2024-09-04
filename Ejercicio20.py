user_input = input("Enter a list of numbers separated by commas: ")

user_list = user_input.split(",")
user_list = [float(num) for num in user_list]

Result = sum(user_list)
print(Result)