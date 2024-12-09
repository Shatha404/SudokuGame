import pygame

SCREEN_WIDTH = 550
SCREEN_LENGTH = 620
background_color = (209, 234, 240)
original_grid_element_color = (0, 0, 0)
buffer = 5


grid = [
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
grid_original = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]

# Solving Sudoku function
def solve_sudoku(window, grid):
    GRID_SIZE = 9  
    def is_valid(row, col, num):
        # Check row and column
        for i in range(GRID_SIZE):
            if grid[row][i] == num or grid[i][col] == num:
                return False

        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if grid[start_row + i][start_col + j] == num:
                    return False

        return True
        
    # to visualize the changes made to the Sudoku grid during the solving process
    def draw_specific_grid(row, col, color):
        pygame.draw.rect(window, color, (50 + col * 50, 50 + row * 50, 50, 50))
        pygame.display.update()

    # to make sure that the blue color will not cover the window
    def draw_number(row, col, value):
        myfont = pygame.font.SysFont('Comic Sans MS', 37)
        number = myfont.render(str(value), True, (0, 0, 0))
        window.blit(number, (50 + col * 50 + 15, 50 + row * 50))

    
    # backtracking algorithm for solving the Sudoku puzzle
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row][col] == 0:
                for num in range(1, GRID_SIZE + 1):
                    if is_valid(row, col, num):
                        grid[row][col] = num
                        draw_specific_grid(row, col, (65, 105, 225))
                        draw_number(row, col, num)
                        pygame.time.delay(100)  # Delay for visualization
                        pygame.event.pump()

                        if solve_sudoku(window, grid): # recursive
                            return True

                        grid[row][col] = 0
                        draw_specific_grid(row, col, (255, 255, 255))
                        pygame.time.delay(100)  # Delay for visualization
                        pygame.event.pump()
                        draw_number(row, col, 0)

                return False

    return True

def main():
    # initaite the window game
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
    pygame.display.set_caption("Sudoku Puzzle Game")
    window.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 37)

    # Draw Sudoku grid
    for i in range(0, 10):
        # Draw grid lines                   #(start coordinate)  #(end coordinate)
        pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 1)  # Vertical line
        pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 1)  # Horizontal line
        if (i % 3 == 0):# thicker lines
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4)
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4)

    # Add a solve button
    solve_button = pygame.Rect(400, 510, 100, 50)
    pygame.draw.rect(window, (128, 128, 128), solve_button)
    solve_text = myfont.render("Solve", True, (0, 0, 0))
    solve_text_rect = solve_text.get_rect(center=solve_button.center)
    window.blit(solve_text, solve_text_rect)

    # Fill the game window with the puzzle numbers
    for i in range(9):
        for j in range(9):
            if (grid[i][j] != 0):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                window.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()
    
    # Game loop 
    solving = False
    while True:
        for event in pygame.event.get():
            # Terminate the game when X button is being pressed    
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # Check if the puzzle was solved
            if solving:
                if not solve_sudoku(window, grid):
                    solving = False
                    print("Sudoku Solved!")
                pygame.time.delay(100)  # Delay for visualization

            # Check if the solve button was clicked
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                if solve_button.collidepoint(pos) and not solving:
                    solving = True

if __name__ == "__main__":
    main()
