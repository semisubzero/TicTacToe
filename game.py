# Example file showing a basic pygame "game loop"
import pygame

if not pygame.font:
    print("Warning, fonts disabled")
if not pygame.mixer:
    print("Warning, sound disabled")

name = 'Player 1'

# Connect to server and get information about players and whose turn it is

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

# Create background
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((170, 238, 187))
pygame.draw.line(background, "white", (266, 50),(266,750), width=10)
pygame.draw.line(background, "white", (533, 50),(533,750), width=10)
pygame.draw.line(background, "white", (50, 266),(750,266), width=10)
pygame.draw.line(background, "white", (50, 533),(750,533), width=10)

# Render title and player names
font = pygame.font.Font(None, 64)
text = font.render("Tic Tac Toe", True, (10, 10, 10))
textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
background.blit(text, textpos)

# X and O sprites
x_sprite = pygame.image.load('x.png')
o_sprite = pygame.image.load('o.png')

# Create board surface
board = pygame.Surface(screen.get_size())
board = board.convert()
board.blit(x_sprite,(100,100))

# Init game logic
boardState = [[0,0,0],[0,0,0],[0,0,0]]

# Function to update board based on boardState
def update_board():
    for i, row in enumerate(boardState):
        for j, cell in enumerate(row):
            if cell == 1:  # Assuming 1 represents X
                screen.blit(x_sprite, (j * 266 + 70, i * 266 + 70))
            elif cell == 2:  # Assuming 2 represents O
                screen.blit(o_sprite, (j * 266 + 70, i * 266 + 70))


while running:
    # poll for events
    pos = None
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # MOUSEBUTTONUP
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

    # Mouse click handling
    if pos:
        # Determine grid position
        grid_x, grid_y = pos[0] // 266, pos[1] // 266
        # Update boardState here based on the player's turn
        # Example: boardState[grid_y][grid_x] = 1
        boardState[grid_y][grid_x] = 1

    # Update the background
    screen.blit(background, (0, 0))
    update_board()

    # Update board state
    #for column in boardState:
     #   for row in column:





    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()