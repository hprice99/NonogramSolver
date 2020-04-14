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

class Line:
    def __init__(self, cells):
        self.cells = cells
    
    def calculateSpan(self):
        pass
        
# Function to extract a list of lines 
def extractLines(lineInput):
    started = False
    lineStarted = False
    lines = [[]]

    for character in lineInput:
        print(character)
        if character == "[" and not started:
            started = True
        
        if started and not lineStarted and character == "[":
            line = []
            lineStarted = True

        if lineStarted and character != "]" and character != "[":
            if character != "," and character != " ":
                line.append(character)
        
        if lineStarted and character == "]":
            lineStarted = False
            lines.append(line)
            print(line)
    
    del lines[0]

    print(lines)
    return lines

board = Board(5, 10)

for i in range(3):
    board.fillCell(1, i, FILL)

for i in range(3):
    board.fillCell(2, i, BLANK)

board.drawBoard()

extractLines("[[4, 5], [5, 2]]")
