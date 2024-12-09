
import time; 
#This is an example SDKboared
SDKboared =[
       [5, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 8, 7, 0, 6, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [0, 5, 0, 0, 6, 1, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 9, 0, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0, 4, 0],
    [9, 0, 0, 0, 4, 8, 7, 0, 0],
    [0, 8, 0, 3, 0, 0, 0, 0, 0]
    ]
#This method is concerned with detecting zero values which represent the yet empty places of the puzzle where the player will guess a correct value to solve the puzzle
def get1stEmpty(SDKboared):
 for i in range(9):
  for j in range(9):
   if SDKboared[i][j]==0:
    return i,j
 return None,None

 
  #This method checks if selected value between 1-9 is a legal value that doesnt violate constraints
def isValValid(SDKboared,canidateVal,row,col):
     
     
     SameRowVals = SDKboared[row]
     if canidateVal in SameRowVals:
        return False
        
     
     
     SameColVals = [SDKboared[i][col] for i in range(9)]
     if canidateVal in SameColVals:
        return False
     row_start = (row // 3) * 3 
     col_start = (col // 3) * 3

     for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if SDKboared[r][c] == canidateVal:
                return False

     return True
 #This method prints the boared    
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
#This method is where suduko solving occuresm it 1)detects the yet not set varibles/places 2)starts gussing 3)repeats the proccess until all done
def Solve(SDKboared):
   
    row,col= get1stEmpty(SDKboared)
    if row is None:
       return True
   
       
    for canidateVal in range(1,10):
       
     if isValValid(SDKboared,canidateVal,row,col):
        SDKboared[row][col]= canidateVal
        if Solve(SDKboared):
            return "Solution!"
     SDKboared[row][col]=0
    return False




start_time = time.time()
print(Solve(SDKboared))
print_SDKboared(SDKboared)
print("Backtrack (Bt) - Time taken:", time.time() - start_time)
