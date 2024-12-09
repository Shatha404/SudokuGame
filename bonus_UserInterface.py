import pygame

SCREEN_WIDTH = 550
SCREEN_LENGTH = 620
background_color = (209, 234, 240)
original_grid_element_color = (0,0,0)
buffer = 5

grid  = [
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

def main():
    # initaite the window game
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_LENGTH))
    pygame.display.set_caption("Sudoku Puzzle Game")
    window.fill(background_color)
    myfont = pygame.font.SysFont('Comic Sans MS', 37)
   
    

    # Draw Sudoku grid
    for i in range(0, 10):                  #(start coordinate)  #(end coordinate) 
        pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 1)# vertical line
        pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 1)# horizontal line
        if (i % 3 == 0): #thicker lines        
            pygame.draw.line(window, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), 4) 
            pygame.draw.line(window, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), 4) 
    
    # fill the game window with the puzzle numbers 
    for i in range(9):
        for j in range(9):
            if (grid[i][j] != 0):
                value = myfont.render(str(grid[i][j]), True, original_grid_element_color)
                window.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50))
    pygame.display.update()
    
    # game loop 
    while True:
        for event in pygame.event.get():
            # mouse and keyboard event handler
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                pos = pygame.mouse.get_pos()
                input_number(window, (pos[0] // 50, pos[1] // 50))

            # terminate the game when X button is being pressed    
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            # The player has won!
            if check_win(grid):
              myfont = pygame.font.SysFont('Comic Sans MS', 50)
              value = myfont.render("you WON genius!", True, (0, 0, 128))
              window.blit(value, (90, 500))
              pygame.display.update()
            
def input_number(window, position):
  i, j = position[1], position[0]
  myfont = pygame.font.SysFont('Comic Sans MS', 37)

  while True:
    # Keep track of events.
    for event in pygame.event.get():

      # Terminate the game when X button is being pressed.
      if event.type == pygame.QUIT:
        return

      # If a keyboard button is being pressed.
      if event.type == pygame.KEYDOWN:
        if(grid_original[i-1][j-1] != 0):
          return

        # If zero is being pressed --> delete the number.
        if (event.key == 48):
          grid[i - 1][j - 1] = 0
          pygame.draw.rect(window, background_color, (
            position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
          pygame.display.update()
          return

        # If a valid input is being pressed --> write it in the puzzle.
        if (0 < event.key - 48 < 10):
          grid[i - 1][j - 1] = event.key - 48
          pygame.draw.rect(window, background_color, (
            position[0] * 50 + buffer, position[1] * 50 + buffer, 50 - 2 * buffer, 50 - 2 * buffer))
          value = myfont.render(str(event.key - 48), True, (3, 37, 120))
          window.blit(value, (position[0] * 50 + 15, position[1] * 50))
          pygame.display.update()
          return

      
def check_win(grid):
  # Check if all the cells are filled.
  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        return False

  # Check for each row
  for row in range(9):
    if len(set(grid[row])) != 9:
      return False

  # Check for each col
  for col in range(9):
    if len(set([grid[row][col] for row in range(9)])) != 9:
      return False

  # Check for each 3*3 subgrids
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      # Create a list of all the numbers in the subgrid
      subgrid = [grid[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]
      if len(set(subgrid)) != 9:
        return False

  return True

if __name__ == "__main__":
    main()