def is_one(check):
    if check[0:3] == 'one':
        return (1)
    return (0)

def is_two(check):
    if check[0:3] == 'two':
        return (1)
    return (0)

def is_three(check):
    if check[0:5] == 'three':
        return (1)
    return (0)

def is_four(check):
    if check[0:4] == 'four':
        return (1)
    return (0)

def is_five(check):
    if check[0:4] == 'five':
        return (1)
    return (0)

def is_six(check):
    if check[0:3] == 'six':
        return (1)
    return (0)

def is_seven(check):
    if check[0:5] == 'seven':
        return (1)
    return (0)

def is_eight(check):
    if check[0:5] == 'eight':
        return (1)
    return (0)

def is_nine(check):
    if check[0:4] == 'nine':
        return (1)
    return (0)

def is_number(check):
    if is_one(check) == 1:
        return (1)
    if is_two(check) == 1:
        return (2)
    if is_three(check) == 1:
        return (3)
    if is_four(check) == 1:
        return (4)
    if is_five(check) == 1:
        return (5)
    if is_six(check) == 1:
        return (6)
    if is_seven(check) == 1:
        return (7)
    if is_eight(check) == 1:
        return (8)
    if is_nine(check) == 1:
        return (9)
    return (0)

with open('input', 'r') as file:
    num = 0
    for line in file:
        index = 0
        while not line[index].isdigit() and is_number(line[index:len(line)]) == 0:
            index += 1
        if is_number(line[index:len(line)]) != 0:
            num += is_number(line[index:len(line)]) * 10
        else:
            num += int(line[index]) * 10
        index = len(line) - 1
        while not line[index].isdigit() and is_number(line[index:len(line)]) == 0:
            index -= 1
        if is_number(line[index:len(line)]) != 0:
            num += is_number(line[index:len(line)])
        else:
            num += int(line[index])
    print(num)
