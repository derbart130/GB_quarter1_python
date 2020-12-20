def int_func():
    phrase = input("Enter the phrase in Latin letters:\n").lower().split()
    result = []
    for word in phrase:
        letts = 0
        for i in word:
            if 97 <= ord(i) <= 122:
                letts += 1
        result.append(word) if letts == len(word) else print(f"{word} - Use only Latin letters!")
    print(f"{' '.join(result).capitalize()}")



int_func()