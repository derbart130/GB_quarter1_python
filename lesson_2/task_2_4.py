string = input("Enter the string: ")
words = string.split()
for ind, word in enumerate(words, 1):
    print(f"{ind}. {word[:10]}")