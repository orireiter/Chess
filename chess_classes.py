from enum import Enum


class Board:
    def __init__(self, gameBoard, state):
        # this is the list of lists, 
        # to be accessed later
        self.gameBoard = gameBoard
        
        # this is the state of the object.
        # meaning, if it's the old 
        # or the new board
        self.state = state

    
    # actions for validation use later on:
    def getBoard(self):
        return self.gameBoard

    def getRow(self, row_num):
        row = self.gameBoard[row_num]
        return row
    
    def getColumn(self, col_num):
        column = []
        for row in self.gameBoard:
            column.append(row[col_num])
        return column


    @staticmethod
    def change_detector(old_board, new_board):
        # this object is created in order to allow checking the type 
        # of the arguments (both need to be board type, such as the example)
        example = Board(["example"],"example")
        if type(old_board) != type(example) or type(new_board) != type(example):
            raise TypeError("At least one of the two arguments is not Board type")
        elif old_board.getBoard() == new_board.getBoard:
            # in case boards are identical
            return None

        

        

class Color(Enum):
    Empty = 0
    White = 1
    Black = 2

class Type(Enum):
    Empty = 0
    Pawn = 1
    King = 2
    Queen = 3
    Bishop = 4
    Knight = 5
    Tower = 6

class Soldier:
    # A soldier class is created to allow conversion from numeral
    # representation on the board, to a soldier and its properties
    # so we can validate its movement.
    def __init__(self, value):
        # The value given is the numeral value on the cell on the board.
        # 1-6 -> white, 7-12 -> black and the type can be easily accessed 
        # through the class with the same name above.
        if value <= 6 and value >= 1:
            self.Color = Color(1)
            self.Type = Type(value)
        elif value >= 7 and value <=12:
            self.Color = Color(2)
            self.Type = Type(value - 6)
        elif value == 0:
            self.Color = Color(value)
            self.Type = Type(value)
            print("An empty cell...")
        else:
            self.Color = None
            self.Type = None
            print("ERROR initializing soldier class")
        print(f"New soldier's characteristics: \nColor - {self.Color.name} \nType - {self.Type.name}")