import time
import queue

class SUDOKU:
    def __init__(self, grid):
        # Initializing the Sudoku board and defining necessary constants and data structures
        grid = ''.join(map(str, [element for row in grid for element in row]))
        self.board = grid
        self.DIGITS = self.COLS = "123456789"
        self.ROWS = "ABCDEFGHI"
        def Product(A, B): return [a + b for a in A for b in B]
        self.SQUARES = Product(self.ROWS, self.COLS)

        # Generating the domains, units, and peers(cells in the same row, the same column, or the same 3x3 subgrid) 
        self.variables = self.SQUARES
        self.domain = self.domainsGen()
        self.values = self.domainsGen()
        self.unitlist = ([Product(self.ROWS, c) for c in self.COLS] + [Product(r, self.COLS) for r in self.ROWS] + [Product(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.SQUARES)
        self.peers = dict((s, set(sum(self.units[s], []))-set([s])) for s in self.SQUARES)
        self.constraints = {(variable, peer) for variable in self.variables for peer in self.peers[variable]}

    # Generating the domains for each cell based on the given board
    def domainsGen(self):
        i = 0
        values = dict()
        for cell in self.variables:
            if self.board[i] != '0':
                values[cell] = self.board[i]
            else:
                values[cell] = self.DIGITS
            i = i + 1
        return values

    # Checking the consistency of a cell's value with its peers
    def consistent(self, x, Xi, Xj):
        for y in self.values[Xj]:
            if Xj in self.peers[Xi] and y != x:
                return True
        return False

    # Revising the domain of a cell based on the consistency of its value with its peers
    def Revise(self, Xi, Xj):
        revised = False
        values = set(self.values[Xi])
        for x in values:
            if not self.consistent(x, Xi, Xj):
                self.values[Xi] = self.values[Xi].replace(x, '')
                revised = True
        return revised

    # Displaying the Sudoku grid
    def gridify(self):
        for r in self.ROWS:
            if r in 'DG': print("------------------------------------------")
            for c in self.COLS:
                if c in '47': print(' | ', self.values[r+c], ' ', end=' ')
                else: print(self.values[r+c], ' ', end=' ') 
            print(end='\n')

    # Checking if the Sudoku grid has been completely solved
    def Completed(self):
        for variable in self.SQUARES:
            if len(self.values[variable]) > 1:
                return False
        return True
    
    # Displaying the solved grid as a single string
    def show(self):
        output = ""
        for variable in self.SQUARES: output = output + self.values[variable]
        return output
    
    # Implementing the AC-3 algorithm for solving the Sudoku puzzle
    def AC3(self):
        q = queue.Queue()
        for arc in self.constraints: q.put(arc)
        solved = True
        while not q.empty():
            (Xi, Xj) = q.get()

            if self.Revise(Xi, Xj):
                if len(self.values[Xi]) == 0:
                    solved = False
                    break

                for Xk in (self.peers[Xi] - set(Xj)):
                    q.put((Xk, Xi))
        return solved

# Main function
if __name__ == "__main__":

    # sudoku puzzle
    grid = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0]
    ]
    sudoku = SUDOKU(grid)
    
    st = time.time()
    solved = sudoku.AC3()
    print("Time taken with AC-3 algorithm: ", time.time()-st)
    
    if sudoku.Completed() and solved:
            print("Puzzle solution:\n")
            sudoku.gridify()
    else:
        print("Failed to solve the grid")
