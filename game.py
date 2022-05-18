from turtle import width
from unittest.util import strclass
from menu import MainMenu
import pygame
from typing import Tuple

class Game:
    def __init__(self):
        pygame.init()

        #  Initialising all variables for later use

        self.WIDTH = 691  # Width of the screen
        self.HEIGHT = 691  # Height of the screen

        self.display = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.window = pygame.display.set_mode(((self.WIDTH, self.HEIGHT)))

        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu

        self.run_app = True  # Boolean responsible for running the whole app 
        self.run_game = True  # Boolean responsible for loop in run_game() 

        #  Keys

        self.RETURN = False
        self.ESC = False

        # Colors

        self.WHITE = (255, 255, 255)

        #  Load assets

        self.board = pygame.image.load('assets/board.jpg')

        #  Apply all assets and variables

        self.screen = pygame.display.set_mode(size=(self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Chess game')

    def start_game(self):

        while self.run_game:
            self.check_input()

            self.display.blit(self.board, (0, 0))

            self.window.blit(self.display,(0, 0))
            pygame.display.update()

            self.reset_keys()

    def check_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_game = False
                self.run_app = False
                self.curr_menu.run_menu = False
                # pygame.quit()
                return
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.RETURN = True
                    return
                if event.key == pygame.K_ESCAPE:
                    self.run_game = False
                    self.run_app = False
                    self.curr_menu.run_menu = False
                    return

    def reset_keys(self):
        self.RETURN = False
        self.ESC = False

    def draw_text(self, text: str, size: int, x: int, y: int):
        self.arial = pygame.font.SysFont('Britannic', size)
        text_surface = self.arial.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
        
