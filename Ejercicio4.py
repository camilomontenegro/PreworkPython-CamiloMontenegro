#Vowel count

string = input("insert any word: ").lower()
count = 0
vowels ="aeiou"
for i in string:
  if i in vowels:
    count += 1

print("The number of vowels is: " + str(count))