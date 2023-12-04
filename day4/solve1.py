with open("input.in", "r") as file:
    total_win = 0
    for line in file:
        parts = line.split(":")
        card_numbers = parts[1].split("|")
        winning_numbers = list(map(int, card_numbers[0].split()))
        my_numbers = list(map(int, card_numbers[1].split()))
        power = -1
        for w in winning_numbers:
            if w in my_numbers:
                power += 1
        card_win = 2 ** power
        if power == -1:
            card_win = 0
        total_win += card_win
        print(card_win)
    print("Total Win: ", total_win)
