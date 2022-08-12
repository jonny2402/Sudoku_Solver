#initialises the board 9x9 matrix of empty lists
rows, cols = (9,9)
board = [[[] for i in range(cols)] for j in range(rows)]
#Each Square represents a 3x3 segment of the sudoku and each of the 9 lists within it represents a cell.
#Each cell is defined by a list of len 2, which points at the coordinates of it on a sudoku eg. [0,0] is top left and [8,8] is the bottom right.
square1 = [[0,0],[0,1],[0,2],
           [1,0],[1,1],[1,2],
           [2,0],[2,1],[2,2]]

square2 = [[0,3],[0,4],[0,5],
           [1,3],[1,4],[1,5],
           [2,3],[2,4],[2,5]]

square3 = [[0,6],[0,7],[0,8],
           [1,6],[1,7],[1,8],
           [2,6],[2,7],[3,8]]

square4 = [[3,0],[3,1],[3,2],
           [4,0],[4,1],[4,2],
           [5,0],[5,1],[5,2]]

square5 = [[3,3],[3,3],[3,5],
           [4,3],[4,3],[4,5],
           [5,3],[5,3],[5,5]]

square6 = [[3,6],[3,7],[3,8],
           [4,6],[4,7],[4,8],
           [6,7],[5,7],[5,8]]

square7 = [[6,0],[6,1],[6,2],
           [7,0],[7,1],[7,2],
           [8,0],[8,1],[8,2]]

square8 = [[6,3],[6,4],[6,5],
           [7,3],[7,4],[7,5],
           [8,3],[8,4],[8,5]]

square9 = [[6,6],[6,7],[6,8],
           [7,6],[7,7],[7,8],
           [8,6],[8,7],[8,8]]

squares = [square1, square2, square3, square4, square5, square6, square7, square8, square9]

#for each cell, there is usually a number of possible numbers available to put in it but by elimination, we remove these.
#Eventually if there gets to only be 1 possible number for a square ie. the length of the list == 1, the cell will be set to that number.

#function to set the number of a cell to it's final value if there is only 1 possiblity by changing it's data format from list to int.
def delist(x,y):
    cell = board[x][y]
    if isinstance(cell, list):
        if len(cell)==1:
            board[x][y] = cell[0]

#function to check if there are any ints in a given row, and then removing any instances of that int from all of the lists in that row.
def row_check():
    for row in range(9):
        for column in range(9):
            cell = board[row][column]
            if isinstance(cell, int):
                x = cell
                for column in range(9):
                    a = row
                    b = column
                    eliminate(a, b, x)
    resolve()

#function to check columns using the same technique as above.
def column_check():
    for column in range(9):
        for row in range(9):
            cell = board[row][column]
            if isinstance(cell, int):
                x = cell
                for row in range(9):
                    a = row
                    b = column
                    eliminate(a, b, x)
    resolve()

#function to check squares.
def square_check():
    for square in squares:
        for cell in square:
            x = board[cell[0]][cell[1]]
            if isinstance(x, int):
                for cell in square:
                    a = cell[0]
                    b = cell[1]
                    eliminate(a, b, x)
    resolve()


#function to check cells for solutions.
def resolve():
    for row in range(9):
        for column in range(9):
            delist(row, column)


#function to eliminate a cell option by removing the given int from it's list.
def eliminate(a, b, x):
    cell = board[a][b]
    if isinstance(cell, list):
        if x in cell:
            cell.remove(x)
            board[a][b] = cell


#basic technique that will check if there is only 1 cell candidate in a row or collumn for any integer.
#eg. if there is only a single 9 present in all of the lists on the top row, that cell must contain a 9.
def hidden_singles_rc_check():
    for row in range(9):
        count = []
        for int in range(1,10):
            for column in range(9):
                if int in board[row][column] and len(count) < 2 :
                    count.append(board[row][column])
                if len(count) == 1:
                    board[row][column] = int
    for column in range(9):
        count = []
        for int in range(1,10):
            for row in range(1,10):
                if int in board[row][column] and len(count) < 2:
                    count.append(board[row][column])
                if len(count) == 1:
                    board[row][column] = int

def hidden_singles_square_check():
    for square in squares:
        count = []
        for i in range(1,10):
            for cell in square:
                if int in board[cell[0]][cell[1]] and len(count) < 2:
                    count.append(board[cell[0]][cell[1]])
            if count == 1:
                cell = count[0]
                board[cell[0]][cell[1]]


#more advanced technique that checks for duplicate cell lists in a square, where if the same number of cells have the same lists that is equal to the length of the list,
#the number of the list must be contained in those squares, thus can be eliminated as possibilities from any other square.
def naked_check():
    for square in squares:
        for cell in square:
            count = 0
            dupe = cell
            for cell in square:
                if cell == dupe:
                    count = count + 1
            if count == len(board[cell[0]][cell[1]]):
                for int in dupe:
                    for cell in square:
                        if cell != dupe:
                            eliminate(cell[0], cell[1], int)

#def omission_check():
#    for row in range(9):



#initialises the board
def initialise_preset():
    rows, cols = (9,9)
    global board 
    board = [[[1,2,3,4,5,6,7,8,9] for i in range(cols)] for j in range(rows)]
    board[0][0]=9
    board[0][2]=4
    board[0][5]=5
    board[0][8]=2
    board[1][2]=7
    board[1][7]=1
    board[2][2]=3
    board[2][3]=2
    board[2][4]=8
    board[3][4]=9
    board[4][3]=8
    board[4][7]=3
    board[4][8]=6
    board[5][0]=5
    board[5][3]=7
    board[5][8]=2
    board[6][0]=1
    board[6][5]=3
    board[6][7]=4
    board[7][5]=6
    board[7][8]=5
    board[8][1]=4
    board[8][8]=9

def check():
    row_check()
    column_check()
    square_check()


#ALTERNATIVE solutions
import numpy as np
print(np.matrix(grid))

def possible(y,x,n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0,9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    print(np.matrix(grid))
    input("More?")

grid = [[0,0,6,2,4,0,0,8,5],
        [0,0,0,6,0,0,0,0,0],
        [0,5,0,7,0,8,0,0,2],
        [1,7,0,0,0,0,0,0,0],
        [3,0,0,0,7,0,0,0,8],
        [0,0,0,9,0,0,0,5,0],
        [0,2,0,0,0,0,0,0,0],
        [8,0,0,0,0,0,6,4,0],
        [0,9,0,0,0,3,8,0,0]]

grid = [[3,9,0,6,5,0,0,0,7],
        [0,6,8,0,0,2,9,0,0],
        [4,0,0,9,0,0,0,0,0],
        [0,0,0,0,0,0,8,0,0],
        [6,7,0,0,0,0,0,4,9],
        [1,0,0,7,4,0,0,0,0],
        [0,4,0,8,0,0,0,3,2],
        [0,0,0,3,7,0,0,0,0],
        [0,5,3,0,2,0,7,0,4]]