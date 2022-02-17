#!/usr/bin/env python
import pprint

# ----------------------------------------------------------------------------#
matrix1 = [
    [7, 1, 8, 5, 3, 2, 9, 4, 6],
    [5, 3, 2, 6, 9, 4, 1, 8, 7],
    [6, 9, 4, 7, 1, 8, 3, 2, 5],
    [1, 2, 7, 3, 4, 5, 8, 6, 9],
    [9, 8, 6, 1, 2, 7, 4, 5, 3],
    [3, 4, 5, 9, 8, 6, 2, 7, 1],
    [4, 6, 3, 8, 7, 9, 5, 1, 2],
    [8, 7, 9, 2, 5, 1, 6, 3, 4],
    [2, 5, 1, 4, 6, 3, 7, 9, 8],
]


# ----------------------------------------------------------------------------#
def verify_sudoku_board(board, value):
    # walk through rows
    for row in range(0, 9):
        if sum(board[row]) != value:
            return False

    # walk through columns
    for col in range(0, 9):
        total = 0
        for row in range(0, 9):
            total += board[row][col]

            if row == 8:
                if total != value:
                    return False

    # walk windows 3x3 - start 0,3,6
    for start in range(0, 9, 3):
        print(start)

        total = 0
        for col in range(start, start + 3):

            for row in range(start, start + 3):
                total += board[row][col]

        if total != value:
            return False

    return True


# ----------------------------------------------------------------------------#
if __name__ == "__main__":
    pp = pprint.PrettyPrinter()
    pp.pprint(matrix1)
    result = verify_sudoku_board(matrix1, 45)
    print(result)
