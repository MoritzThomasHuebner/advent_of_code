from copy import deepcopy

player_1_cards = []
player_2_cards = []

with open('day_22_input.txt', 'r') as f:
    dealing_to = 1
    for line in f.readlines():
        line = line.replace('\n', '')
        if line in ["Player 1:", ""]:
            continue
        elif line == "Player 2:":
            dealing_to += 1
        elif dealing_to == 1:
            player_1_cards.append(int(line))
        elif dealing_to == 2:
            player_2_cards.append(int(line))

while len(player_1_cards) != 0 and len(player_2_cards) != 0:
    player_1_card = player_1_cards[0]
    player_2_card = player_2_cards[0]

    player_1_cards.remove(player_1_card)
    player_2_cards.remove(player_2_card)

    if player_1_card > player_2_card:
        player_1_cards.append(player_1_card)
        player_1_cards.append(player_2_card)
    else:
        player_2_cards.append(player_2_card)
        player_2_cards.append(player_1_card)

if len(player_1_cards) > len(player_2_cards):
    winner_cards = player_1_cards
else:
    winner_cards = player_2_cards

result = 0
for i in range(1, len(winner_cards) + 1):
    result += winner_cards[-i] * i
print(result)

# Part 2
player_1_cards = []
player_2_cards = []

with open('day_22_input.txt', 'r') as f:
    dealing_to = 1
    for line in f.readlines():
        line = line.replace('\n', '')
        if line in ["Player 1:", ""]:
            continue
        elif line == "Player 2:":
            dealing_to += 1
        elif dealing_to == 1:
            player_1_cards.append(int(line))
        elif dealing_to == 2:
            player_2_cards.append(int(line))

class Configuration(object):

    def __init__(self, cards_1, cards_2):
        self.cards_1 = cards_1
        self.cards_2 = cards_2

    def __eq__(self, other):
        return self.cards_1 == other.cards_1 and self.cards_2 == other.cards_2


def play_game(cards_1, cards_2):
    configurations = []
    winner = 0
    c_1 = deepcopy(cards_1)
    c_2 = deepcopy(cards_2)
    while winner == 0:
        c_1, c_2, winner = play_round(deepcopy(c_1), deepcopy(c_2), configurations)
    return c_1, c_2, winner


def play_round(cards_1, cards_2, configurations):
    p1_cards = deepcopy(cards_1)
    p2_cards = deepcopy(cards_2)

    config = Configuration(deepcopy(p1_cards), deepcopy(p2_cards))
    if config in configurations:
        return p1_cards, p2_cards, 1
    configurations.append(config)

    if len(p1_cards) == 0:
        return p1_cards, p2_cards, 2
    elif len(p2_cards) == 0:
        return p1_cards, p2_cards, 1

    player_1_card = p1_cards[0]
    player_2_card = p2_cards[0]
    p1_cards.remove(player_1_card)
    p2_cards.remove(player_2_card)

    if player_1_card <= len(p1_cards) and player_2_card <= len(p2_cards):
        _, _, winner = play_game(cards_1=deepcopy(p1_cards[:player_1_card]), cards_2=deepcopy(p2_cards[:player_2_card]))
        if winner == 1:
            p1_cards.append(player_1_card)
            p1_cards.append(player_2_card)
        elif winner == 2:
            p2_cards.append(player_2_card)
            p2_cards.append(player_1_card)
        else:
            raise ValueError
    else:
        if player_1_card > player_2_card:
            p1_cards.append(player_1_card)
            p1_cards.append(player_2_card)
        else:
            p2_cards.append(player_2_card)
            p2_cards.append(player_1_card)

    if len(p2_cards) == 0:
        winner = 1
    elif len(p1_cards) == 0:
        winner = 2
    else:
        winner = 0

    return p1_cards, p2_cards, winner

player_1_cards, player_2_cards, w = play_game(player_1_cards, player_2_cards)
print(player_1_cards)
print(player_2_cards)
print(w)

if len(player_1_cards) > len(player_2_cards):
    winner_cards = player_1_cards
else:
    winner_cards = player_2_cards

result = 0
for i in range(1, len(winner_cards) + 1):
    result += winner_cards[-i] * i
print(result)