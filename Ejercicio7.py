first = float(input("Insert the first number: "))
operator = input("Operation: ")
second = float(input("Second number: "))

if operator == "+":
  first += second
elif operator == "-":
  first += -(second)
elif operator == "/":
  first /= second
elif operator == "*":
  first *= second

print(first)