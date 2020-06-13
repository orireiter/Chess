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
        elif old_board.getBoard() == new_board.getBoard():
            # in case boards are identical
            print("error: identical boards")
            return False
        else:
            old_board = old_board.getBoard()
            new_board = new_board.getBoard()
            # assuming everything went well up to this part
            # we'll first compare each row in both boards
            rang1 = range(8)
            different_rows = []
            for row in rang1:
                if old_board[row] != new_board[row]:
                    different_rows.append(row)
            
            # after appending, the list should contain
            # 1 or 2 rows, otherwise - it's an illegal move
            if len(different_rows) < 0 or len(different_rows) > 2 :
                print("error: bad move, too many rows changed")
                return False
            # when 1 row is different there should be 
            # 2 cells that were changed in it
            elif len(different_rows) == 1:
                row_num = different_rows[0]
                # assigning the rows into variables
                old_row = old_board[row_num]
                new_row = new_board[row_num]
                
                # running through the 2 rows looking for
                # differences, should be exactly 2
                different_cells = []
                for cell in rang1:
                    if old_row[cell] != new_row[cell]:
                        different_cells.append(cell)
                if len(different_cells) != 2 :
                    print("error: bad move, not 2 cells were changed")
                    return False
                else:
                    # returning a dict with key = row and 
                    # value = the cells a that are different  
                    return {f"{row_num}": different_cells}
            elif len(different_rows) == 2:
                # assigning te rows' nums
                row_num1 = different_rows[0]
                row_num2 = different_rows[1]  

                # there should be 1 change in each row
                different_cells1 = []
                different_cells2 = []
                for cell1 in rang1:
                    # applying a check to the 1st row given
                    if old_board[row_num1][cell1] != new_board[row_num1][cell1]:
                        different_cells1.append(cell1)
                    # applying to the 2nd
                    if old_board[row_num2][cell1] != new_board[row_num2][cell1]:
                        different_cells2.append(cell1)

                if len(different_cells1) != 1  or  len(different_cells2) != 1 :
                    print("error: bad move, an invalid amount of cells were changed")
                    return False
                else:
                    return {f"{row_num1}": different_cells1,
                            f"{row_num2}": different_cells2}        


    @staticmethod
    def who_moved(old_board, new_board, cells_dict):
        # to check who moved, of the two cells changed,
        # i'll which cell became 0 in the latest board
        # this is the check when there was a change in only 1 row
        if len(cells_dict) == 1:
            row_num = list(cells_dict.keys())
            row_num = int(row_num[0])
            old_row = old_board.getRow(row_num)
            new_row = new_board.getRow(row_num)

            cell_nums = list(cells_dict.values())
            print(cell_nums)
            cell_num1 = cell_nums[0][0]
            cell_num2 = cell_nums[0][1]
            old_cell1 = old_row[cell_num1]
            old_cell2 = old_row[cell_num2]

            new_cell1 = new_row[cell_num1]
            new_cell2 = new_row[cell_num2]

            if old_cell1 != 0 and new_cell1 == 0:
                if old_cell1 == new_cell2:
                    return old_cell1, {"old": [row_num,cell_num1], "new": [row_num, cell_num2]}
                else:
                    print("error: problem recgonizing soldier moved")
                    return False
            elif old_cell2 != 0 and new_cell2 == 0:
                if old_cell2 == new_cell1:
                    return old_cell2, {"old": [row_num,cell_num2], "new": [row_num, cell_num1]}
                else:
                    print("error: problem recgonizing soldier moved"    )
                    return False
            else:
                print("error: problem recgonizing soldier moved")
                return False
        elif len(cells_dict) == 2:
            row_nums = list(cells_dict.keys())
            row_num1 = int(row_nums[0])
            row_num2 = int(row_nums[1])

            old_row = old_board.getRow(row_num1)
            new_row = new_board.getRow(row_num1)

            old_cell1 = old_row[cells_dict[row_nums[0]][0]]
            new_cell1 = new_row[cells_dict[row_nums[0]][0]]
            # print(old_cell1, new_cell1)
            ########################################
            
            old_row = old_board.getRow(row_num2)
            new_row = new_board.getRow(row_num2)

            old_cell2 = old_row[cells_dict[row_nums[1]][0]]
            new_cell2 = new_row[cells_dict[row_nums[1]][0]]
            # print(old_cell2, new_cell2)
            #########################################

            if old_cell1 != 0 and new_cell1 == 0:
                if old_cell1 == new_cell2:
                    return old_cell1, {
                        "old": [row_num1,cells_dict[row_nums[0]][0]], 
                        "new": [row_num2,cells_dict[row_nums[1]][0] ]}
                else:
                    print("error: problem recgonizing soldier moved")
                    return False
            elif old_cell2 != 0 and new_cell2 == 0:
                if old_cell2 == new_cell1:
                    return old_cell2, {
                        "old": [row_num1,cells_dict[row_nums[1]][0]], 
                        "new": [row_num2,cells_dict[row_nums[0]][0] ]}
                else:
                    print("error: problem recgonizing soldier moved")
                    return False
            


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
    def __init__(self, value, old_cell, new_cell):
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
        
        self.old_cell = old_cell
        self.new_cell = new_cell
        
        print(f"New soldier's characteristics: \nColor - {self.Color.name} \nType - {self.Type.name} \nOld Cell - {self.old_cell} \nNew Cell - {self.new_cell}")
