#Tip Tracker 15%
sub_total = float(input("Insert the total amount: "))
tip = 0.15
total = (sub_total * tip) + sub_total

print("You have to pay: " + str(total) + " €")