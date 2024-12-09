import time
 
   # Check if the chosen number is a valid choice at [row, col] for the cell
def isValValid(board, row, col, num):
    # 1- Check row if nothing match return true
    if num in board[row]:
        return False
    # 2- Check column if nothing match return true
    if num in [board[i][col] for i in range(9)]:
        return False
    # 3- Check 3x3 subgrid if nothing match return true
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    return True


   
def getPos(SDKboared, poss) :
 
 for i in range(len (SDKboared)):
  for j in range(len(SDKboared)):
   if SDKboared[i][j]==poss:
    
    return i,j
 return None,None

def getRow(SDKboared, poss) :
 
 for i in range(9):
  for j in range(9):
   if SDKboared[i][j]==poss:
    
    return i
 return 0




  # Solve sudoku puzzle by using Forward Checking algorithm
def solve_sudoku_fc(SDKboared):
   



        # Solve sudoku puzzle by using BT if needed
    empty_cell = find_empty_cell(SDKboared)
    if not empty_cell:
        return True  # If all cells filled, solution for sudoku puzzle is founded
    row, col = empty_cell
       
    for canidateVal in range(1,10):
       
     if isValValid(SDKboared,row,col,canidateVal):
        SDKboared[row][col]= canidateVal
     if forward_check1(SDKboared, row, col, canidateVal) and solve_sudoku_fc(SDKboared):
            return True
     
     SDKboared[row][col]=0
    return False


def forward_check1(SDKboared, row, column, number):
   
  
    # Check if there a duplicate values in the same row or  column if duplicate is found then block
    for check_row in range(9):
        for check_col in range(9):
              
            if (
                    (check_row == row and SDKboared[check_row][check_col] == number and check_col != column) or
                    (check_col == column and SDKboared[check_row][check_col] == number and check_row != row) or
                    (check_row // 3 == row // 3 and check_col // 3 == column // 3 and
                     SDKboared[check_row][check_col] == number and (check_row != row or check_col != column))
            ):
                return False 
                      

    return True


def find_empty_cell(board):
    # Find the next empty cell in the board , if there is no empty return None
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

 # Function to print a Sudoku board
def print_SDKboared(SDKboared):
    for i in range(len(SDKboared)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(SDKboared[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(SDKboared[i][j])
            else:
                print(str(SDKboared[i][j]) + " ", end="")
 

# MAIN FUNCTION 
puzzle1 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]



solved_fc = [row[:] for row in puzzle1]
start_time = time.time()
solve_sudoku_fc(solved_fc)
print("Forward Checking (FC) - Time taken:", time.time() - start_time)
print_SDKboared(solved_fc)
