data = input("Insert the width and height separated by commas: ")

values = data.split(",")

width = float(values[0].strip())
height = float(values[1].strip())

area = width * height
print("The area is: ", area)