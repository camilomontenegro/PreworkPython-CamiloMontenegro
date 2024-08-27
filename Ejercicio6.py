#Palindrome checker
my_string = input("Try and type something: ")
my_string = my_string.casefold()
my_rev_string =  reversed(my_string)

if list(my_string) == list(my_rev_string):
  print("It is a palindrome!!")
else:
  print("Keep trying")

