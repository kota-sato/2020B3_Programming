with open("dataset/data.txt", "r", encoding = 'shift-jis') as f:
    line = f.readline()
    while line:
        print(line)
        line = f.readline()