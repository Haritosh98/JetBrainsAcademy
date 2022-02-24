import random

domino_set = []
for i in range(0, 7):
    for j in range(i, 7):
        domino_set.append([i, j])
random.shuffle(domino_set)

comp = []
play = []
domino = []
stock_pieces = random.sample(domino_set, 14)
computer_pieces = random.sample(domino_set, 7)
player_pieces = random.sample(domino_set, 7)

print('Stock:', stock_pieces)

for i in computer_pieces:
    if i[0] == i[1]:
        comp.append(i)

for i in player_pieces:
    if i[0] == i[1]:
        play.append(i)

if sum(max(comp)) > sum(max(play)):
    domino_snake = max(comp)
    domino.append(domino_snake)
    position = computer_pieces.index(max(comp))
    computer_pieces = computer_pieces[:position] + computer_pieces[position + 1:]
    print('Computer pieces:', computer_pieces)
    print('Player pieces:', player_pieces)
    print('Domino snake:', domino)
    print('Status: player')
else:
    domino_snake = max(play)
    domino.append(domino_snake)
    position = player_pieces.index(max(play))
    player_pieces = player_pieces[:position] + player_pieces[position + 1:]
    print('Computer pieces:', computer_pieces)
    print('Player pieces:', player_pieces)
    print('Domino snake:', domino)
    print('Status: computer')
