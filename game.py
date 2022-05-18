from pickle import FALSE
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
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

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

        #  Black

        self.black_pawn = pygame.image.load('assets/figures/black_pawn.png')

        #  White
        
        self.white_pawn_1 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_2 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_3 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_4 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_5 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_6 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_7 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_pawn_8 = pygame.image.load('assets/figures/white_pawn.png')
        self.white_knight_1 = pygame.image.load('assets/figures/white_knight.png')
        self.white_knight_2 = pygame.image.load('assets/figures/white_knight.png')
        self.white_bishop_1 = pygame.image.load('assets/figures/white_bishop.png')
        self.white_bishop_2 = pygame.image.load('assets/figures/white_bishop.png')
        self.white_rook_1 = pygame.image.load('assets/figures/white_rook.png')
        self.white_rook_2 = pygame.image.load('assets/figures/white_rook.png')
        self.white_king = pygame.image.load('assets/figures/white_king.png')
        self.white_queen = pygame.image.load('assets/figures/white_queen.png')


        self.curr_y = 543
        self.curr_x = 68


        self.temp_y = self.curr_y

        self.figures = {self.white_pawn_1: (68, self.temp_y), self.white_pawn_2: (147, self.temp_y), self.white_pawn_3: (226, self.temp_y),
                        self.white_pawn_4: (305, self.temp_y), self.white_pawn_5: (384, self.temp_y), self.white_pawn_6: (461, self.temp_y),
                        self.white_pawn_7: (539, self.temp_y), self.white_pawn_8: (617, self.temp_y)}
        
        #  Apply all assets and variables

        pygame.display.set_caption('Chess game')     


    def start_game(self):

        while self.run_game:
            self.check_input()
            self.check_event()

            self.display.blit(self.board, (0, 0))
            

            #  Draw sprites of figures
            
            for key, value in self.figures.items():
                self.draw_sprite(key, value[0], value[1])

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
                    self.ESC = True
                    return
                if event.key == pygame.K_LEFT:
                    self.LEFT = True
                    return
                if event.key == pygame.K_RIGHT:
                    self.RIGHT = True
                    return
                if event.key == pygame.K_UP:
                    self.UP = True
                    return
                if event.key == pygame.K_DOWN:
                    self.DOWN = True
                    return

    def check_event(self):
        if self.ESC:
            self.run_game = False
            self.curr_menu.run_menu = True
        if self.UP:
            self.curr_y -= 1
        if self.DOWN:
            self.curr_y += 1
        if self.RIGHT:
            self.curr_x += 1
        if self.LEFT:
            self.curr_x -= 1


    def reset_keys(self):
        self.RETURN = False
        self.ESC = False
        self.RIGHT = False
        self.LEFT = False
        self.UP = False
        self.DOWN = False

    def draw_text(self, text: str, size: int, x: int, y: int):
        self.arial = pygame.font.SysFont('Britannic', size)
        text_surface = self.arial.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
        
    def draw_sprite(self, image, x: int, y: int):
        image_rect = image.get_rect()
        image_rect.center = (x, y)
        self.display.blit(image, image_rect)
