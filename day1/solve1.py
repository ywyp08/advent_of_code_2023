with open('input', 'r') as file:
    num = 0
    for line in file:
        index = 0;
        while not line[index].isdigit():
            index += 1
        num += int(line[index]) * 10
        index = len(line) - 1
        while not line[index].isdigit():
            index -= 1
        num += int(line[index])
    print(num)
