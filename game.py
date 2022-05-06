import pygame

class Game:
    def __init__(self):
        pygame.init()

        #  Initialising all variables for later use

        self.WIDTH = 700  # Width of the screen
        self.HEIGHT = 800  # Height of the screen

        self.run_game = True  # Boolean responsible for game_loop

        #  Apply all assets and variables

        self.screen = pygame.display.set_mode(size=(self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Chess game')

        



#  Prototype of the game loop
while run:

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            break
