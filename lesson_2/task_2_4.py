string = input("Enter the string: ")
words = string.split()
for ind, el in enumerate(words, 1):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, el[:10])
