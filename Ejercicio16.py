def input_to_list(input_string):
  num_list = input_string.split(',')
  num_list = [int(num.strip()) for num in num_list]
  return num_list


def count_odd_even(num_list):
  odd_count = 0
  even_count = 0
  odd_numbers = []
  even_numbers = []


  for num in num_list:
    if num % 2 == 0:
      even_count += 1
      even_numbers.append(num)
    else:
      odd_count += 1
      odd_numbers.append(num)
  return odd_count, even_count, odd_numbers, even_numbers  


input_string = input("Enter numbers separated by commas: ")
num_list = input_to_list(input_string)
odd_count, even_count, odd_numbers, even_numbers = count_odd_even(num_list)

print(f"There are {odd_count} ({odd_numbers}) odd numbers and {even_count} ({even_numbers}) even numbers")