with open("input.in", "r") as file:
    cards = [1] * 190
    card = 0
    for line in file:
        parts = line.split(":")
        card_numbers = parts[1].split("|")
        winning_numbers = list(map(int, card_numbers[0].split()))
        my_numbers = list(map(int, card_numbers[1].split()))
        card += 1
        matches = 0
        for w in winning_numbers:
            if w in my_numbers:
                matches += 1
        if matches > 0:
            cards[card:card + matches] = [x + cards[card-1] for x in cards[card:card + matches]]
        print(matches)
    print(sum(cards))
