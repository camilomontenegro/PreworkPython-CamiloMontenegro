def count_words(prompt):
  result = prompt.split()  
  word_count = 0
  for i in result:
    word_count += 1
  return word_count

def main():
  prompt = input("Enter a string: ")
  word_count = count_words(prompt)
  print(f"There are {word_count} words in here")


if __name__ == "__main__":
  main()







