user_inp = list("         ")  # this is the empty grid


def grid(inp):
    """This is the game grid"""
    return f"---------\n| {' '.join(inp[0:3])} |\n| {' '.join(inp[3:6])} |\n| {' '.join(inp[6:])} |\n---------"


def game_state(inp):   # should the prints be returns instead?
    """This decides if won, impossible, not finished or draw"""
    str_form = ''.join(inp[0])+''.join(inp[1])+''.join(inp[2])
    soln = [str_form[0:3], str_form[3:6], str_form[6:], str_form[0:7:3], str_form[1:8:3], str_form[2::3], str_form[0::4], str_form[2:7:2]]
    if soln.count("XXX") + soln.count("OOO") == 1:
        for i in soln:
            if i == "XXX":
                return "X wins"
            elif i == "OOO":
                return "O wins"
    if soln.count("XXX") + soln.count("OOO") >= 2:
        return "Impossible"
    elif abs(str_form.count("O") - str_form.count("X") >= 2) or abs(str_form.count("X") - str_form.count("O") >= 2):
        return "Impossible"
    elif soln.count("XXX") + soln.count("OOO") == 0:
        if str_form.count(" ") >= 1:
            return "Game not finished"
        elif str_form.count(' ') == 0:
            return "Draw"


print(grid(inp=user_inp))


map = [user_inp[0:3], user_inp[3:6], user_inp[6:]]


occupied = False

count = 0

while not occupied:

    count = count + 1

    # print(map)

    # game_state(inp=user_inp)

    pos = input("Enter the coordinates: ").split(" ")
    #print(pos)

    for num in pos:
        try:
            int(num)
        except ValueError:
            print("You should enter numbers!")
            continue

    vertical = int(pos[0]) - 1
    horizontal = int(pos[1]) - 1

    if (not 0 < int(pos[0]) < 4) or (not 0 < int(pos[1]) < 4):
        print("Coordinates should be from 1 to 3!")
        continue
    elif map[vertical][horizontal] == "X" or map[vertical][horizontal] == "O":
        print("This cell is occupied! Choose another one!")
    else:
        if count%2 != 0:
            map[vertical][horizontal] = "X"
            print(f"---------\n| {' '.join(map[0])} |\n| {' '.join(map[1])} |\n| {' '.join(map[2])} |\n---------")
        elif count%2 == 0:
            map[vertical][horizontal] = "O"
            print(f"---------\n| {' '.join(map[0])} |\n| {' '.join(map[1])} |\n| {' '.join(map[2])} |\n---------")

    if game_state(inp=map) == "Game not finished": # or game_state(inp=map) == "Draw":
        continue
    else:
        print(game_state(inp=map))
        break
