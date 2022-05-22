# imports
import numpy as np
import copy

# classes
class Board():
    board = None
    valid = None
    points = 0
    moves = 0
    tokens = []

    def __init__(self) -> None:
       a = np.zeros(100, dtype='int') 
       self.board = a.reshape(10, 10)
       self.valid = True

       tokens_list = [Token_One, Token_Two, Token_Three, Token_Four, Token_Five]
       for token in tokens_list:
        self.tokens.append(token)

    # actions  
    def whipe(self):
        a = np.zeros(100) 
        self.board = a.reshape(10, 10)

    def draw(self):
        print(self.board)

    def check_erase(self):
        to_erease = []
        # horizontal
        for y, row in enumerate(self.board):
            if not 0 in row:
                for x, _ in enumerate(row):
                    # elments to remove full row in board
                    to_erease.append({'x' : x, 'y' : y})
                    
        # vertical
        # copy board
        c = copy.deepcopy(self.board)

        # swap columns and rows
        swap = c.transpose()

        # check for 0 in columns (rows)
        for x, column in enumerate(swap):
            if not 0 in column:
                for y, _ in enumerate(column):
                    # elments to remove full column in board
                    to_erease.append({'x' : x, 'y' : y})

        # actual removal
        for remove in to_erease:
            self.board[remove['y'][remove['x']]]

# Tokens
class Token():
    token = None
    width = None
    height = None
    filled = None
    color = None

    def draw(self):
        print(self.token)

class Token_Big_Square(Token):
    '''
    111
    111
    111
    '''
    def __init__(self) -> None:
        self.width = 3
        self.height = 3
        self.filled = 9
        self.color = 1

        a = np.ones(self.width * self.width)
        self.token = a.reshape(self.width, self.width)

class Token_Big_L(Token):
    '''
    100
    100
    111
    '''
    def __init__(self) -> None:
        self.width = 3
        self.height = 3
        self.filled = 5
        self.color = 2

        a = np.zeros(self.width * self.width)
        b = a.reshape(self.width, self.width)

        b[0][0] = self.color
        b[1][0] = self.color

        b[2][0] = self.color
        b[2][1] = self.color
        b[2][2] = self.color

        self.token = b

class Token_Vertical_Mirrored_Big_L(Token):
    '''
    001
    001
    111
    '''
    def __init__(self) -> None:
        self.width = 3
        self.height = 3
        self.filled = 5
        self.color = 2

        a = np.zeros(self.width * self.width)
        b = a.reshape(self.width, self.width)

        b[0][2] = self.color
        b[1][2] = self.color

        b[2][0] = self.color
        b[2][1] = self.color
        b[2][2] = self.color

        self.token = b

class Token_Horizontal_Mirrored_Big_L(Token):
    '''
    111
    100
    100
    '''
    def __init__(self) -> None:
        self.width = 3
        self.height = 3
        self.filled = 5
        self.color = 2

        a = np.zeros(self.width * self.width)
        b = a.reshape(self.width, self.width)

        b[0][0] = self.color
        b[0][1] = self.color
        b[0][2] = self.color

        b[1][0] = self.color
        b[2][0] = self.color

        self.token = b

class Token_Horizontal_Vertikal_Mirrored_Big_L(Token):
    '''
    111
    001
    001
    '''
    def __init__(self) -> None:
        self.width = 3
        self.height = 3
        self.filled = 5
        self.color = 2

        a = np.zeros(self.width * self.width)
        b = a.reshape(self.width, self.width)

        b[0][0] = self.color
        b[0][1] = self.color
        b[0][2] = self.color

        b[1][2] = self.color
        b[2][2] = self.color

        self.token = b

class Token_Six(Token):
    ''''''
    def __init__(self) -> None:
        self.width = 1
        self.height = 5
        self.filled = 5
        self.color = 3

        a = np.zeros(5)
        a[0] = self.color
        a[1] = self.color
        a[2] = self.color
        a[3] = self.color
        a[4] = self.color

        b = a.reshape(5, 1)
        self.token = b

class Token_Five(Token):
    # len 5 stick horizontal
    def __init__(self) -> None:
        self.width = 5
        self.height = 1
        self.filled = 5
        self.color = 3

        a = np.zeros(5)
        a[0] = self.color
        a[1] = self.color
        a[2] = self.color
        a[3] = self.color
        a[4] = self.color

        self.token = a

class Token_Six(Token):
    # len 4 stick vertikal
    def __init__(self) -> None:
        self.width = 1
        self.height = 4
        self.filled = 4
        self.color = 3

        a = np.zeros(4)
        a[0] = self.color
        a[1] = self.color
        a[2] = self.color
        a[3] = self.color

        b = a.reshape(4, 1)
        self.token = b

        