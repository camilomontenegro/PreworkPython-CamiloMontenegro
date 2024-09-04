# price = float(input("Enter a price: "))
# discount = 0.2
# total = price - (price * discount)

# print(f"{total} is your total!")

def cal_discount(price, discount):
  total = price - (price * discount)
  return total

price = float(input("Enter a price: "))
discount = 0.2
total = cal_discount(price, discount)

print(f"{total} is your total!")