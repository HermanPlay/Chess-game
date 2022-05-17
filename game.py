from menu import MainMenu
import pygame

class Game:
    def __init__(self):
        pygame.init()

        #  Initialising all variables for later use

        self.WIDTH = 700  # Width of the screen
        self.HEIGHT = 800  # Height of the screen

        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu

        self.run_app = True  # Boolean responsible for running the whole app 
        self.run_game = True  # Boolean responsible for loop in run_game() 

        self.RETURN = False

        #  Apply all assets and variables

        self.screen = pygame.display.set_mode(size=(self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Chess game')

    def start_game(self):
        self.check_input()
        self.reset_keys()
        

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
                self.run_app = False
                # pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.RETURN = True

    def reset_keys(self):
        self.RETURN = False
