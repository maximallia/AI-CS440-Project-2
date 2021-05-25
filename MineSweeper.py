import copy
import sys
from random import randint
from matplotlib import pyplot as plt

'''
    Kyle VanWageninge kjv48
    Daniel Ying dty16
    AI Project 2 Mine Sweeper
'''


# place the mines randomly around the board
def PlaceMines(mine_sweeper, sweeper_size, mines):
    i = 0
    while i in range(mines):
        x_mine = randint(0, sweeper_size - 1)
        y_mine = randint(0, sweeper_size - 1)
        if mine_sweeper[x_mine][y_mine] == 0:
            mine_sweeper[x_mine][y_mine] = 1
        else:
            i = i - 1
        i = i + 1
    return mine_sweeper


# place hints on a hint board
def PlaceHints(mine_sweeper, sweeper_size):
    hint_sweeper = [[0 for _ in range(sweeper_size)] for _ in range(sweeper_size)]

    for i in range(sweeper_size):
        for k in range(sweeper_size):
            x = i
            y = k
            if mine_sweeper[i][k] == 1:
                hint_sweeper[i][k] = 'M'
            else:
                num_mines = 0
                if x + 1 < sweeper_size and mine_sweeper[x + 1][y] == 1:
                    num_mines = num_mines + 1
                if y + 1 < sweeper_size and mine_sweeper[x][y + 1] == 1:
                    num_mines = num_mines + 1
                if x - 1 > -1 and mine_sweeper[x - 1][y] == 1:
                    num_mines = num_mines + 1
                if y - 1 > -1 and mine_sweeper[x][y - 1] == 1:
                    num_mines = num_mines + 1
                if x + 1 < sweeper_size and y + 1 < sweeper_size and mine_sweeper[x + 1][y + 1] == 1:
                    num_mines = num_mines + 1
                if x - 1 > -1 and y - 1 > -1 and mine_sweeper[x - 1][y - 1] == 1:
                    num_mines = num_mines + 1
                if x + 1 < sweeper_size and y - 1 > -1 and mine_sweeper[x + 1][y - 1] == 1:
                    num_mines = num_mines + 1
                if y + 1 < sweeper_size and x - 1 > -1 and mine_sweeper[x - 1][y + 1] == 1:
                    num_mines = num_mines + 1
                # adds the (clue, clear_identified, mines_identified, hidden)
                hint_sweeper[i][k] = (num_mines, 0, 0, SurroundingSquares(x, y, sweeper_size))

    return hint_sweeper


# return how many squares surrounding a given cell
def SurroundingSquares(x, y, sweeper_size):
    squares = 0
    if x + 1 < sweeper_size:
        squares = squares + 1
    if y + 1 < sweeper_size:
        squares = squares + 1
    if x - 1 > -1:
        squares = squares + 1
    if y - 1 > -1:
        squares = squares + 1
    if x + 1 < sweeper_size and y + 1 < sweeper_size:
        squares = squares + 1
    if x - 1 > -1 and y - 1 > -1:
        squares = squares + 1
    if x + 1 < sweeper_size and y - 1 > -1:
        squares = squares + 1
    if y + 1 < sweeper_size and x - 1 > -1:
        squares = squares + 1
    return squares


# will update each neighbor of the mine found
def MineUpdate(hint_sweeper, sweeper_size, x, y):
    hints = hint_sweeper.copy()
    if x + 1 < sweeper_size and hints[x + 1][y] != 'M':
        hints[x + 1][y] = list(hints[x + 1][y])
        hints[x + 1][y][2] = hints[x + 1][y][2] + 1
        hints[x + 1][y][3] = hints[x + 1][y][3] - 1
    if y + 1 < sweeper_size and hints[x][y + 1] != 'M':
        hints[x][y + 1] = list(hints[x][y + 1])
        hints[x][y + 1][2] = hints[x][y + 1][2] + 1
        hints[x][y + 1][3] = hints[x][y + 1][3] - 1
    if x - 1 > -1 and hints[x - 1][y] != 'M':
        hints[x - 1][y] = list(hints[x - 1][y])
        hints[x - 1][y][2] = hints[x - 1][y][2] + 1
        hints[x - 1][y][3] = hints[x - 1][y][3] - 1
    if y - 1 > -1 and hints[x][y - 1] != 'M':
        hints[x][y - 1] = list(hints[x][y - 1])
        hints[x][y - 1][2] = hints[x][y - 1][2] + 1
        hints[x][y - 1][3] = hints[x][y - 1][3] - 1
    if x + 1 < sweeper_size and y + 1 < sweeper_size and hints[x + 1][y + 1] != 'M':
        hints[x + 1][y + 1] = list(hints[x + 1][y + 1])
        hints[x + 1][y + 1][2] = hints[x + 1][y + 1][2] + 1
        hints[x + 1][y + 1][3] = hints[x + 1][y + 1][3] - 1
    if x - 1 > -1 and y - 1 > -1 and hints[x - 1][y - 1] != 'M':
        hints[x - 1][y - 1] = list(hints[x - 1][y - 1])
        hints[x - 1][y - 1][2] = hints[x - 1][y - 1][2] + 1
        hints[x - 1][y - 1][3] = hints[x - 1][y - 1][3] - 1
    if x + 1 < sweeper_size and y - 1 > -1 and hints[x + 1][y - 1] != 'M':
        hints[x + 1][y - 1] = list(hints[x + 1][y - 1])
        hints[x + 1][y - 1][2] = hints[x + 1][y - 1][2] + 1
        hints[x + 1][y - 1][3] = hints[x + 1][y - 1][3] - 1
    if y + 1 < sweeper_size and x - 1 > -1 and hints[x - 1][y + 1] != 'M':
        hints[x - 1][y + 1] = list(hints[x - 1][y + 1])
        hints[x - 1][y + 1][2] = hints[x - 1][y + 1][2] + 1
        hints[x - 1][y + 1][3] = hints[x - 1][y + 1][3] - 1
    return hints


# will update each neighbor of a clear square found
# don't update each of the clear neighbors just yet, this will be done when the clear square gets queried
def ClearUpdate(hint_sweeper, sweeper_size, x, y):
    hints = hint_sweeper.copy()
    hints[x][y] = list(hints[x][y])

    if x + 1 < sweeper_size and hints[x + 1][y] != 'M':
        hints[x + 1][y] = list(hints[x + 1][y])
        hints[x + 1][y][1] = hints[x + 1][y][1] + 1
        hints[x + 1][y][3] = hints[x + 1][y][3] - 1
    if y + 1 < sweeper_size and hints[x][y + 1] != 'M':
        hints[x][y + 1] = list(hints[x][y + 1])
        hints[x][y + 1][1] = hints[x][y + 1][1] + 1
        hints[x][y + 1][3] = hints[x][y + 1][3] - 1
    if x - 1 > -1 and hints[x - 1][y] != 'M':
        hints[x - 1][y] = list(hints[x - 1][y])
        hints[x - 1][y][1] = hints[x - 1][y][1] + 1
        hints[x - 1][y][3] = hints[x - 1][y][3] - 1
    if y - 1 > -1 and hints[x][y - 1] != 'M':
        hints[x][y - 1] = list(hints[x][y - 1])
        hints[x][y - 1][1] = hints[x][y - 1][1] + 1
        hints[x][y - 1][3] = hints[x][y - 1][3] - 1
    if x + 1 < sweeper_size and y + 1 < sweeper_size and hints[x + 1][y + 1] != 'M':
        hints[x + 1][y + 1] = list(hints[x + 1][y + 1])
        hints[x + 1][y + 1][1] = hints[x + 1][y + 1][1] + 1
        hints[x + 1][y + 1][3] = hints[x + 1][y + 1][3] - 1
    if x - 1 > -1 and y - 1 > -1 and hints[x - 1][y - 1] != 'M':
        hints[x - 1][y - 1] = list(hints[x - 1][y - 1])
        hints[x - 1][y - 1][1] = hints[x - 1][y - 1][1] + 1
        hints[x - 1][y - 1][3] = hints[x - 1][y - 1][3] - 1
    if x + 1 < sweeper_size and y - 1 > -1 and hints[x + 1][y - 1] != 'M':
        hints[x + 1][y - 1] = list(hints[x + 1][y - 1])
        hints[x + 1][y - 1][1] = hints[x + 1][y - 1][1] + 1
        hints[x + 1][y - 1][3] = hints[x + 1][y - 1][3] - 1
    if y + 1 < sweeper_size and x - 1 > -1 and hints[x - 1][y + 1] != 'M':
        hints[x - 1][y + 1] = list(hints[x - 1][y + 1])
        hints[x - 1][y + 1][1] = hints[x - 1][y + 1][1] + 1
        hints[x - 1][y + 1][3] = hints[x - 1][y + 1][3] - 1
    return hints


# go through and add 'M' (mine tag) to all surrounding squares marked as hidden
# then update each new mine position's neighbors
def HiddenMine(game_sweeper, hint_sweeper, x, y, sweeper_size):
    hints = hint_sweeper.copy()
    if x + 1 < sweeper_size and game_sweeper[x + 1][y] == '?':
        game_sweeper[x + 1][y] = 'M'
        hints = MineUpdate(hints, sweeper_size, x + 1, y)
    if y + 1 < sweeper_size and game_sweeper[x][y + 1] == '?':
        game_sweeper[x][y + 1] = 'M'
        hints = MineUpdate(hints, sweeper_size, x, y + 1)
    if x - 1 > -1 and game_sweeper[x - 1][y] == '?':
        game_sweeper[x - 1][y] = 'M'
        hints = MineUpdate(hints, sweeper_size, x - 1, y)
    if y - 1 > -1 and game_sweeper[x][y - 1] == '?':
        game_sweeper[x][y - 1] = 'M'
        hints = MineUpdate(hints, sweeper_size, x, y - 1)
    if x + 1 < sweeper_size and y + 1 < sweeper_size and game_sweeper[x + 1][y + 1] == '?':
        game_sweeper[x + 1][y + 1] = 'M'
        hints = MineUpdate(hints, sweeper_size, x + 1, y + 1)
    if x - 1 > -1 and y - 1 > -1 and game_sweeper[x - 1][y - 1] == '?':
        game_sweeper[x - 1][y - 1] = 'M'
        hints = MineUpdate(hints, sweeper_size, x - 1, y - 1)
    if x + 1 < sweeper_size and y - 1 > -1 and game_sweeper[x + 1][y - 1] == '?':
        game_sweeper[x + 1][y - 1] = 'M'
        hints = MineUpdate(hints, sweeper_size, x + 1, y - 1)
    if y + 1 < sweeper_size and x - 1 > -1 and game_sweeper[x - 1][y + 1] == '?':
        game_sweeper[x - 1][y + 1] = 'M'
        hints = MineUpdate(hints, sweeper_size, x - 1, y + 1)
    return hints


# go through and add 'c' (clear tag) to all surrounding squares marked as hidden
def HiddenSafe(game_sweeper, hint_sweeper, x, y, sweeper_size):
    hints = hint_sweeper.copy()

    if x + 1 < sweeper_size and game_sweeper[x + 1][y] == '?':
        game_sweeper[x + 1][y] = 'c'
    if y + 1 < sweeper_size and game_sweeper[x][y + 1] == '?':
        game_sweeper[x][y + 1] = 'c'
    if x - 1 > -1 and game_sweeper[x - 1][y] == '?':
        game_sweeper[x - 1][y] = 'c'
    if y - 1 > -1 and game_sweeper[x][y - 1] == '?':
        game_sweeper[x][y - 1] = 'c'
    if x + 1 < sweeper_size and y + 1 < sweeper_size and game_sweeper[x + 1][y + 1] == '?':
        game_sweeper[x + 1][y + 1] = 'c'
    if x - 1 > -1 and y - 1 > -1 and game_sweeper[x - 1][y - 1] == '?':
        game_sweeper[x - 1][y - 1] = 'c'
    if x + 1 < sweeper_size and y - 1 > -1 and game_sweeper[x + 1][y - 1] == '?':
        game_sweeper[x + 1][y - 1] = 'c'
    if y + 1 < sweeper_size and x - 1 > -1 and game_sweeper[x - 1][y + 1] == '?':
        game_sweeper[x - 1][y + 1] = 'c'
    return hints


# go through all the hidden_cells remaining in the board and find the one with the lowest amount of total clues
# surrounding that hidden square
def BetterRandom(game, hidden_cells, sweeper_size):
    position_lowest = [-1, -1]
    lowest_score = 65
    print(hidden_cells)
    for i in range(len(hidden_cells)):
        squares = 0
        print(hidden_cells[i][0], hidden_cells[i][1])
        if hidden_cells[i][0] + 1 < sweeper_size:
            if game[hidden_cells[i][0] + 1][hidden_cells[i][1]] != '?' and \
                    game[hidden_cells[i][0] + 1][hidden_cells[i][1]] != 'M':
                squares = squares + game[hidden_cells[i][0] + 1][hidden_cells[i][1]]
        if hidden_cells[i][1] + 1 < sweeper_size:
            if game[hidden_cells[i][0]][hidden_cells[i][1] + 1] != '?' and \
                    game[hidden_cells[i][0]][hidden_cells[i][1] + 1] != 'M':
                squares = squares + game[hidden_cells[i][0]][hidden_cells[i][1] + 1]
        if hidden_cells[i][0] - 1 > -1:
            if game[hidden_cells[i][0] - 1][hidden_cells[i][1]] != '?' and \
                    game[hidden_cells[i][0] - 1][hidden_cells[i][1]] != 'M':
                squares = squares + game[hidden_cells[i][0] - 1][hidden_cells[i][1]]
        if hidden_cells[i][1] - 1 > -1:
            if game[hidden_cells[i][0]][hidden_cells[i][1] - 1] != '?' and \
                    game[hidden_cells[i][0]][hidden_cells[i][1] - 1] != 'M':
                squares = squares + game[hidden_cells[i][0]][hidden_cells[i][1] - 1]
        if hidden_cells[i][0] + 1 < sweeper_size and hidden_cells[i][1] + 1 < sweeper_size:
            if game[hidden_cells[i][0] + 1][hidden_cells[i][1] + 1] != '?' and \
                    game[hidden_cells[i][0] + 1][hidden_cells[i][1] + 1] != 'M':
                squares = squares + game[hidden_cells[i][0] + 1][hidden_cells[i][1] + 1]
        if hidden_cells[i][0] - 1 > -1 and hidden_cells[i][1] - 1 > -1:
            if game[hidden_cells[i][0] - 1][hidden_cells[i][1] - 1] != '?' and \
                    game[hidden_cells[i][0] - 1][hidden_cells[i][1] - 1] != 'M':
                squares = squares + game[hidden_cells[i][0] - 1][hidden_cells[i][1] - 1]
        if hidden_cells[i][0] + 1 < sweeper_size and hidden_cells[i][1] - 1 > -1:
            if game[hidden_cells[i][0] + 1][hidden_cells[i][1] - 1] != '?' and \
                    game[hidden_cells[i][0] + 1][hidden_cells[i][1] - 1] != 'M':
                squares = squares + game[hidden_cells[i][0] + 1][hidden_cells[i][1] - 1]
        if hidden_cells[i][1] + 1 < sweeper_size and hidden_cells[i][0] - 1 > -1:
            if game[hidden_cells[i][0] - 1][hidden_cells[i][1] + 1] != '?' and \
                    game[hidden_cells[i][0] - 1][hidden_cells[i][1] + 1] != 'M':
                squares = squares + game[hidden_cells[i][0] - 1][hidden_cells[i][1] + 1]
        print(squares)
        if squares <= lowest_score and squares != 0:
            lowest_score = squares
            position_lowest = [hidden_cells[i][0], hidden_cells[i][1]]

    return position_lowest


# basic sweeper agent
def basic_agent(game_sweeper, hint_sweeper, size):
    game = game_sweeper.copy()
    game_holder = []
    hints = hint_sweeper.copy()
    print()

    run = 0
    mines_hit = 0
    while run < 1000:
        run = run + 1
        print(run)
        # print current game board and hints board on each run
        for i in range(size):
            print()
            for k in range(size):
                print(game[i][k], end=" ")
        for i in range(size):
            print()
            for k in range(size):
                print(hints[i][k], end=" ")
        # give x and y a default start
        x = -1
        y = -1
        low_hidden = 9
        # iterate over the board to find a clear square to query, choose the one with the least amount
        # of hidden squares
        for i in range(size):
            for k in range(size):
                if game[i][k] == 'c':
                    hints[i][k] = list(hints[i][k])
                    if hints[i][k][3] < low_hidden:
                        low_hidden = hints[i][k][3]
                        x = i
                        y = k
        # if no 'c' was found, run through the rest of the board on old clues to see if any new information
        # can be gained based on info gathered from clear cells
        if x == -1:
            for i in range(size):
                for k in range(size):
                    # check for old clues with squares still hidden
                    # don't update based on current cell because it had already been queried and updated
                    if game[i][k] != '?' and game[i][k] != 'M' and game[i][k] != 'c':
                        x = i
                        y = k
                        if (hints[x][y][0] - hints[x][y][2]) == (hints[x][y][3]) and hints[x][y][3] > 0:
                            print('run2')
                            game[x][y] = hints[x][y][0]
                            hints[x][y] = list(hints[x][y])
                            hints = HiddenMine(game, hints, x, y, size)
                        elif ((SurroundingSquares(x, y, size) - hints[x][y][0]) - hints[x][y][1]) == (
                                hints[x][y][3]) and hints[x][y][3] > 0:
                            print('yes2')
                            print(x, y)
                            print(hints[x][y][1], hints[x][y][3])
                            game[x][y] = hints[x][y][0]
                            hints[x][y] = list(hints[x][y])
                            hints = HiddenSafe(game, hints, x, y, size)

            x = -1
        # set x back to default params then start looking for another 'c' after old clues have been iterated over
        for i in range(size):
            for k in range(size):
                if game[i][k] == 'c':
                    print('c', i, k)
                    hints[i][k] = list(hints[i][k])
                    if hints[i][k][3] < low_hidden:
                        low_hidden = hints[i][k][3]
                        x = i
                        y = k
        # if no new clear square came up then we have to find a random square that hasn't been queried yet
        # make a list of (x,y) pairs that haven't been hit yet and randomly choose one
        # if list is empty the board is complete
        if x == -1:
            print('randnum')
            game_holder.clear()
            for i in range(size):
                for k in range(size):
                    if game[i][k] == '?':
                        game_holder.append((i, k))
            if game_holder:

                cell = BetterRandom(game, game_holder, size)
                print(cell)
                x = cell[0]
                y = cell[1]
                # s = input()
                
                if x == -1:

                    t = randint(0, len(game_holder) - 1)
                    hold = game_holder.pop(t)
                    x = hold[0]
                    y = hold[1]
                    print(t)

            else:
                break
        print(x, y)
        # if the x,y was a mine, update the board and add a count to mines blown up
        if hints[x][y] == 'M':
            game[x][y] = 'M'
            hints = MineUpdate(hints, size, x, y)
            mines_hit = mines_hit + 1
        # if x, y is a value skip it(this shouldn't happen but just in case)
        if game[x][y] != 'c' and game[x][y] != '?':
            print('nope')
        # if clue - mines_identified == hidden_squares all hidden squares are mines
        # mark all as such and update info
        elif (hints[x][y][0] - hints[x][y][2]) == (hints[x][y][3]) and hints[x][y][3] != 0:
            print('run')
            game[x][y] = hints[x][y][0]
            hints[x][y] = list(hints[x][y])
            hints = HiddenMine(game, hints, x, y, size)
            hints = ClearUpdate(hints, size, x, y)
        # if surrounding_squares - clue - clear_identified == hidden_squares all hidden squares are clear
        # mark all as such and update info
        elif ((SurroundingSquares(x, y, size) - hints[x][y][0]) - hints[x][y][1]) == (hints[x][y][3]) and hints[x][y][
            3] != 0:
            print('yes')
            print(hints[x][y][1], hints[x][y][3])
            game[x][y] = hints[x][y][0]
            hints[x][y] = list(hints[x][y])
            hints = HiddenSafe(game, hints, x, y, size)
            hints = ClearUpdate(hints, size, x, y)
        # if no further information can be gathered from the clue update information and choose a new x, y
        else:
            game[x][y] = hints[x][y][0]
            hints = ClearUpdate(hints, size, x, y)
    print('hit mines', mines_hit)
    return game, mines_hit


# add knowledge to the knowledge base
def AddKnowledge(KB, game_sweeper, hint_sweeper, x, y, mine, sweeper_size):
    game = game_sweeper.copy()
    # will insert what we know so far
    # KB.insert(0, (x, y, mine))
    equation = []
    # create an equation from surrounding squares of the clue
    if mine == 0:
        print('run')
        mines_in = 0
        if x + 1 < sweeper_size:
            if game[x + 1][y] == '?' or game[x + 1][y] == 'c':
                equation.append((x + 1, y, 0, -1))
            elif game[x + 1][y] == 'M':
                # equation.append((x + 1, y, 1, 1))
                mines_in = mines_in + 1
        if y + 1 < sweeper_size:
            if game[x][y + 1] == '?' or game[x][y + 1] == 'c':
                equation.append((x, y + 1, 0, -1))
            elif game[x][y + 1] == 'M':
                # equation.append((x, y + 1, 1, 1))
                mines_in = mines_in + 1
        if x - 1 > -1:
            if game[x - 1][y] == '?' or game[x - 1][y] == 'c':
                equation.append((x - 1, y, 0, -1))
            elif game[x - 1][y] == 'M':
                # equation.append((x - 1, y, 1, 1))
                mines_in = mines_in + 1
        if y - 1 > -1:
            if game[x][y - 1] == '?' or game[x][y - 1] == 'c':
                equation.append((x, y - 1, 0, -1))
            elif game[x][y - 1] == 'M':
                # equation.append((x, y - 1, 1, 1))
                mines_in = mines_in + 1
        if x + 1 < sweeper_size and y + 1 < sweeper_size:
            if game[x + 1][y + 1] == '?' or game[x + 1][y + 1] == 'c':
                equation.append((x + 1, y + 1, 0, -1))
            elif game[x + 1][y + 1] == 'M':
                # equation.append((x + 1, y + 1, 1, 1))
                mines_in = mines_in + 1
        if x - 1 > -1 and y - 1 > -1:
            if game[x - 1][y - 1] == '?' or game[x - 1][y - 1] == 'c':
                equation.append((x - 1, y - 1, 0, -1))
            elif game[x - 1][y - 1] == 'M':
                # equation.append((x - 1, y - 1, 1, 1))
                mines_in = mines_in + 1
        if x + 1 < sweeper_size and y - 1 > -1:
            if game[x + 1][y - 1] == '?' or game[x + 1][y - 1] == 'c':
                equation.append((x + 1, y - 1, 0, -1))
            elif game[x + 1][y - 1] == 'M':
                # equation.append((x + 1, y - 1, 1, 1))
                mines_in = mines_in + 1
        if y + 1 < sweeper_size and x - 1 > -1:
            if game[x - 1][y + 1] == '?' or game[x - 1][y + 1] == 'c':
                equation.append((x - 1, y + 1, 0, -1))
            elif game[x - 1][y + 1] == 'M':
                # equation.append((x - 1, y + 1, 1, 1))
                mines_in = mines_in + 1
        # add clue to the end of the equation and place in the kb - the number of mines uncovered to add to equation
        # ex. unhidden mines = 1 ==> ? + ? + ? = clue-1 because we will not be putting an uncovered square in the eq
        equation.append(game[x][y] - mines_in)
        KB.append(equation)

        # iterate over the knowledge base and remove any cells that are not hidden anymore
        # if removing a mine position from the kb you will also -1 from the last value in the equation
        # ex ? + 1 + ? + 1 = 2 ==> ? + ? = 0
    for i in range(len(KB)):
        if len(KB[i]) > 1:
            for t in range(len(KB[i]) - 1):
                KB[i][t] = list(KB[i][t])
                # print(x, y)
                if KB[i][t][3] == 0 or KB[i][t][3] == 1 or (KB[i][t][0] == x and KB[i][t][1] == y):
                    KB[i].pop(t)
                    KB[i][len(KB[i]) - 1] = KB[i][len(KB[i]) - 1] - mine
                    break
    print('current kb')
    for i in range(len(KB)):
        print(KB[i])
        print()

    return game


# check if any basic inference can be made
def Inference(game_sweeper, KB, size, hint_sweeper):
    changed = True
    holder = []
    # looks for equations where the clue = 0 (all cells are clear)
    # looks for equations where # vars in equation = clue (all cells are mines)
    # near them
    while changed:
        changed = False
        i = 0
        while i in range(len(KB)):

            total = 0

            for t in range(len(KB[i]) - 1):
                KB[i][t] = list(KB[i][t])
                total = total + KB[i][t][2]
            if total == KB[i][len(KB[i]) - 1] or total != KB[i][len(KB[i]) - 1]:

                # if the total is 0 then each position is clear
                # mark them as 'c' on the game board to be queried by the agent
                if total == 0 and KB[i][len(KB[i]) - 1] == 0:
                    changed = True
                    # print(KB[i])
                    for s in range(len(KB[i]) - 1):
                        KB[i][0] = list(KB[i][0])
                        # KB[i][0][3] = KB[i][0][2]
                        clear_location = KB[i].pop(0)
                        game_sweeper[clear_location[0]][clear_location[1]] = 'c'
                    del KB[i]
                    i = i - 1

                # if the total is >0 and the amount of hidden cells = the total, then each position is mine
                # mark them as 'M' on the game board and add them to the KB
                elif len(KB[i]) - 1 == KB[i][len(KB[i]) - 1]:
                    changed = True
                    # print(KB[i])
                    for s in range(len(KB[i]) - 1):
                        KB[i][0] = list(KB[i][0])
                        # KB[i][0][3] = KB[i][0][2]
                        mine_location = KB[i].pop(0)
                        game_sweeper[mine_location[0]][mine_location[1]] = 'M'
                        game_sweeper = AddKnowledge(KB, game_sweeper, hint_sweeper, mine_location[0], mine_location[1],
                                                    1,
                                                    size)
                    del KB[i]
                    i = i - 1
            i = i + 1
    print('current in')
    for i in range(len(KB)):
        print(KB[i])
        print()


# create subsets from the knowledge base
def CreateSubsets(KB):
    changed2 = True
    chacha = 0
    while changed2:
        changed2 = False
        i = 0

        while i in range(len(KB)):
            new_subset = []
            for t in range(len(KB[i])):
                new_subset.append(KB[i][t])
            s = 0
            # take the supposed subset and check if it is a subset of any equation in the knowledge base
            while s < len(KB):
                KB[s], changed = isSub(KB, new_subset, i, KB[s], s)
                if changed == 1:
                    chacha = 1
                s = s + 1
            i = i + 1

    # if chacha == 1:
    # Inference(game_sweeper, KB, size, hint_sweeper)

    return chacha


# check to see if the list1 is a subset of list2
def isSub(KB, subset, index, equation, equation_index):
    in_subset = 0
    changed = 0
    print('in subset')
    print(subset)
    print(equation)
    if index != equation_index and len(equation) >= len(subset):
        for i in range(len(subset) - 1):
            for k in range(len(equation) - 1):
                if subset[i] == equation[k]:
                    in_subset = in_subset + 1

        if in_subset == len(subset) - 1:
            changed = 1
            equation[len(equation) - 1] = equation[len(equation) - 1] - subset[len(subset) - 1]
            for a in range(len(subset) - 1):
                equation.remove(subset[a])

    return equation, changed


# will combine multiple equations that have the same variables
def backtrack(KB2):
    all_equations = []
    KB = copy.deepcopy(KB2)
    print('current in')
    x_pos = -1
    y_pos = -1
    for i in range(len(KB)):
        print(KB[i])
        print()

    for i in range(len(KB)):
        unique_values = []
        indexes = [i]
        equation = []
        solutions = []
        # get a base equation
        for s in range(len(KB[i])):
            equation.append(KB[i][s])
            unique_values.append(KB[i][s])
        unique_values.pop()
        e_length = len(equation) - 1
        # look through the rest of the equations to see if any has vars in common
        # if so add it to the new equation and update indexes to say not to add that equation again
        for t in range(e_length):
            for s in range(len(KB)):
                if s != i and s not in indexes:
                    # print('current values inside', i, KB[s])
                    for k in range(len(KB[s])):

                        if equation[t] == KB[s][k]:
                            # print('runnung', k)
                            indexes.append(s)
                            clue = equation.pop()
                            for x in range(len(KB[s])):
                                equation.append(KB[s][x])
                            equation[len(equation) - 1] = equation[len(equation) - 1] + clue
        print('equation:', equation)
        # if the length of the equation is different from when it started it means one or more equations was added to
        # to the original equation
        if e_length != len(equation) - 1:
            run_amount = 2 ** len(unique_values)
            # convert a binary string into a list
            for binary in range(run_amount):
                number = "{0:016b}".format(binary)
                b_i = []
                b_i[:0] = number
                print(b_i)
                # s = input()
                if binary != 0:
                    # taking that binary list iterate over the new equation and find suitable solutions
                    for index in range(len(unique_values)):
                        # print(unique_values)
                        unique_values[index][2] = b_i.pop()
                    # print(unique_values)
                    for w in range(len(unique_values) - 1):
                        x = unique_values[w][0]
                        y = unique_values[w][1]
                        bit = unique_values[w][2]
                        for z in range(len(equation) - 1):
                            if equation[z][0] == x and equation[z][1] == y:
                                equation[z][2] = bit
                    sum1 = 0
                    # check if the sum of the new equation after putting in the 0s and 1s see if it matches the clue
                    for check in range(len(equation) - 1):
                        sum1 = sum1 + int(equation[check][2])
                    if sum1 == equation[len(equation) - 1]:
                        unique = copy.deepcopy(unique_values)
                        solutions.append(unique)
            # only send solutions if there are more than 3 to give a good number of samples
            if len(solutions) > 3:
                print('run prob solutions')
                run, x_pos, y_pos = ProbClear(solutions)
                if run == 1:
                    break
        if x_pos != -1:
            break
            # s = len(KB[t])
        print('equation:', equation)

    return x_pos, y_pos


# given a set of possible solutions from backtracking find a var that has prob over 85% of being clear
def ProbClear(solutions):
    update = 0
    total = len(solutions)
    print(total)
    x = -1
    y = -1
    for i in range(len(solutions[0])):
        clear = 0
        for k in range(len(solutions)):
            if solutions[k][i][2] == '0':
                clear = clear + 1
        '''
        for sol in range(len(solutions)):
            print(sol)
            print(solutions[sol])
        print(clear)
        '''
        if clear / total > .84:
            print(solutions[0][i])
            x = solutions[0][i][0]
            y = solutions[0][i][1]
            update = 1
            break
    return update, x, y


def advanced_agent(game_sweeper, hint_sweeper, size):
    KB = []
    game = game_sweeper.copy()
    game_holder = []
    hints = hint_sweeper.copy()
    print()
    run = 0
    mines_hit = 0
    while run < 3000:
        run = run + 1
        for i in range(size):
            print()
            for k in range(size):
                print(game[i][k], end=" ")
        x = -1
        y = -1
        low_hidden = 9
        # look for a clear cell
        for i in range(size):
            for k in range(size):
                if game[i][k] == 'c':
                    print('c', i, k)
                    hints[i][k] = list(hints[i][k])
                    if hints[i][k][3] < low_hidden:
                        low_hidden = hints[i][k][3]
                        x = i
                        y = k
                        print('current x, y', x, y)
        # if no clear cells could be found try creating subsets from the current KB information
        if x == -1 and run != 1:
            again = 1
            x = -2
            sub_run = 0
            # goes until no more subsets can be created
            # will run inference on each iteration
            while again == 1:
                again = CreateSubsets(KB)
                sub_run = sub_run + again
                print(sub_run)
                if again == 1:
                    Inference(game, KB, size, hints)

            if sub_run == 0:
                x = -1

        # if subsets could not be created run backtracking algo
        if x == -1 and run != 1:
            x, y = backtrack(KB)
            print('BACKTRACK', x, y)

        # if no clear cells or subsets or backtracking doesn't reveal anything pick randomly
        if x == -1 or run == 1:
            print('randnum')
            game_holder.clear()
            for i in range(size):
                for k in range(size):
                    if game[i][k] == '?':
                        game_holder.append((i, k))
            if game_holder:
                '''
                cell = BetterRandom(game, game_holder, size)
                print(cell)
                x = cell[0]
                y = cell[1]
                # s = input()
                if x == -1:
                    '''
                t = randint(0, len(game_holder) - 1)
                hold = game_holder.pop(t)
                x = hold[0]
                y = hold[1]
                print(t)
            else:
                break
        if x != -2:
            # if cell is a mine
            if hints[x][y] == 'M':
                game[x][y] = 'M'
                game = AddKnowledge(KB, game, hints, x, y, 1, size)
                Inference(game, KB, size, hints)
                mines_hit = mines_hit + 1
            else:
                game[x][y] = hints[x][y][0]
                game = AddKnowledge(KB, game, hints, x, y, 0, size)
                Inference(game, KB, size, hints)
        x = -1
    return game, mines_hit


def main():
    # dim of MineSweeper and number of mines
    size = int(sys.argv[1])
    num_mines = int(sys.argv[2])

    # Initialize the minesweeper array with given size
    sweeper_og = [[0 for _ in range(size)] for _ in range(size)]

    sweeper_copy = sweeper_og.copy()

    # place the mines
    final_sweeper = PlaceMines(sweeper_copy, size, num_mines)
    # use the placed mines to place hints
    hint_sweeper = PlaceHints(final_sweeper, size)
    for i in range(size):
        print()
        for k in range(size):
            print(hint_sweeper[i][k], end=" ")

    # create the game board
    game_sweeper = [['?' for _ in range(size)] for _ in range(size)]
    print(game_sweeper)
    # send in the game board and the hint board into the basic agent and get the finished board
    new_sweeper, success = basic_agent(game_sweeper, hint_sweeper, size)
    # new_sweeper, success = advanced_agent(game_sweeper, hint_sweeper, size)
    for i in range(size):
        print()
        for k in range(size):
            print(hint_sweeper[i][k][0], end=" ")
    print()
    for i in range(size):
        print()
        for k in range(size):
            print(new_sweeper[i][k], end=" ")
    print()
    print('mines exploded:', success)
    print('mines avoided:', num_mines - success)
    print('success rate =', (num_mines - success) / num_mines)

    # for testing averages

    squares = size * size
    tests = [int(squares * .1), int(squares * .2), int(squares * .3), int(squares * .4), int(squares * .5),
             int(squares * .6),
             int(squares * .7), int(squares * .8), int(squares * .9)]

    average = []
    '''
    for i in range(len(tests)):
        total_rate = 0
        for k in range(100):
            sweeper_og = [[0 for _ in range(size)] for _ in range(size)]
            sweeper_copy = sweeper_og.copy()
            final_sweeper = PlaceMines(sweeper_copy, size, tests[i])
            hint_sweeper = PlaceHints(final_sweeper, size)
            game_sweeper = [['?' for _ in range(size)] for _ in range(size)]
            new_sweeper, success = basic_agent(game_sweeper, hint_sweeper, size)
            # new_sweeper, success = advanced_agent(game_sweeper, hint_sweeper, size)
            rate = (tests[i] - success) / tests[i]
            total_rate = total_rate + rate
        average.append(total_rate / 100)
    '''
    print(average)

    test = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    basic_average = [99, 93, 79, 64, 55, 49, 43, 37, 26]
    advanced_average = [99, 98, 86, 71, 60, 51, 45, 37, 26]
    basic_improved = [99, 95, 86, 69, 62, 55, 51, 41, 27]
    advanced_improved = [99, 98, 90, 80, 71, 62, 54, 43, 27]

    plt.plot(test, basic_average, color='blue', label='Basic Agent')
    plt.plot(test, advanced_average, color='red', label='Advanced Agent')
    plt.plot(test, basic_improved, color='green', label='Basic Agent Improved Random')
    plt.plot(test, advanced_improved, color='orange', label='Advanced Agent Improved Random')

    plt.xlabel('Mine Density(%)')
    plt.ylabel('Success Rate(%)')
    plt.title('Average Final score vs Density')
    plt.legend()
    plt.show()


main()
