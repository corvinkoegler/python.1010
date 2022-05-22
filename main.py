# imports
from re import T
import classes
import random
import copy

# code
# inits
board = classes.Board()
init_tokens = []

for i, cls in enumerate(board.tokens):
    token = board.tokens[i]()
    init_tokens.append(token)

active_tokens = []
while board.valid:
    # generate active tokens
    if(not active_tokens):
        for i in range(3):
            active_tokens.append(init_tokens[random.randint(0, len(init_tokens) -1)])

    # draw
    board.draw()

    for token in active_tokens:
        print("")
        token.draw()

    # select 
    choice_token = input("Choose Option: ")
    print("")

    # choose
    active_token = active_tokens[int(choice_token) -1]

    # place
    placed = False
    active_coordinates = {"x" : 0, "y" : 0}
    
    while not placed:
        # make copy of gae board
        show = copy.deepcopy(board)

        # simplify visuals (damn humans!)
        for x, row in enumerate(show.board):
            for y, element in enumerate(row):
                if element != 0:
                    show.board[x][y] = 1

        # draw token
        if active_token.token.ndim == 2:
            for y, row in enumerate(active_token.token):
                for x, element in enumerate(row):
                    x_coordinate = active_coordinates["x"] + x
                    y_coordinate = active_coordinates["y"] + y

                    if element != 0:
                        show.board[y_coordinate][x_coordinate] += 2

        elif active_token.token.ndim == 1:
            for x, element in enumerate(row):
                x_coordinate = active_coordinates["x"] + x
                y_coordinate = active_coordinates["y"] + y

                if element != 0:
                    show.board[y_coordinate][x_coordinate] += 2
        
        # draw state
        show.draw()
        print("")

        # check if direction is valid
        valid_direction = False
        bypass = False

        while not valid_direction:
            direction = input("-l --left | -r right | -u --up | -d --down | <enter> confirm | -b --back: ")

            # left move
            if direction == "-l" or direction == "--left":
                if active_coordinates["x"] -1 >= 0:
                    active_coordinates["x"] -= 1
                    valid_direction = True
                else:
                    print("GAME: Coordinates out of bounds, try another option.")

            # right move
            elif direction == "-r" or direction == "--right":
                if (active_coordinates["x"] + active_token.width + 1) <= 10:
                    active_coordinates["x"] += 1
                    valid_direction = True
                else:
                    print("GAME: Coordinates out of bounds, try another option.")

            # up move
            elif direction == "-u" or direction == "--up":
                if (active_coordinates["y"] - 1) >= 0:
                    active_coordinates["y"] -= 1
                    valid_direction = True
                else:
                    print("GAME: Coordinates out of bounds, try another option.")

            # down move
            elif direction == "-d" or direction == "--down":
                if (active_coordinates["y"] + active_token.height + 1) <= 10:
                    active_coordinates["y"] += 1
                    valid_direction = True
                else:
                    print("GAME: Coordinates out of bounds, try another option.")

            # back move
            elif direction == "-b" or direction == "--back":
                bypass = True
                placed = True
                valid_direction = True

            # confirm move
            elif direction == "":
                if not 3 in show.board:

                    # place token
                    for y, row in enumerate(active_token.token):
                        for x, element in enumerate(row):
                            x_coordinate = active_coordinates["x"] + x
                            y_coordinate = active_coordinates["y"] + y

                            board.board[y_coordinate][x_coordinate] += element

                    board.check_erase()
                    
                    active_tokens.remove(active_token)
                    valid_direction = True
                    placed = True

                else:
                    print("GAME: Can't do that here. Maybe a space is already occupied.")

# TODO multi directon vanish fixen (Zu löschende erst an Liste anhängen, dann gesammelt löschen)
