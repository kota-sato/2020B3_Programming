with open("dataset/data.txt", "r", encoding = 'shift-jis') as f:
    for line in f:
        print(line, end="")