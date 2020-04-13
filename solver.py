#!/usr/bin/env python3

from array import *

CELL_UNDEFINED = '*'
CELL_FILL = '#'
CELL_BLANK = '.'

UNDEFINED = 0
FILL = 1
BLANK = 2


class Board:

    def __init__(self, rows, columns):
        """
        Initialise the board
        :param rows: The number of rows for this board.
        :param white: The number of columns for this board.
        """
        self.rows = rows
        self.columns = columns

        # Create a 2D array to store the board
        self.board = [[CELL_UNDEFINED for i in range(columns)] for j in range(rows)]

    def fillCell(self, row, column, type):
        if type == FILL:
            self.board[row][column] = CELL_FILL
        elif type == BLANK:
            self.board[row][column] = CELL_BLANK
    
    def drawBoard(self):
        for i in range(self.rows):
            for j in range(self.columns):
                # Print the cells on this row side-by-side
                print(self.board[i][j], end='')
            
            # Print a new line
            print('')

board = Board(5, 10)

for i in range(3):
    board.fillCell(1, i, FILL)

for i in range(3):
    board.fillCell(2, i, BLANK)

board.drawBoard()
