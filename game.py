from menu import MainMenu
import pygame
from dataclasses import dataclass

@dataclass
class Figure:
    def __init__(self, rank: str, color: bool, image: str, pos: str, first_move: bool, pov, selected: bool = False):
        self.rank = rank
        self.color = color
        self.image = pygame.image.load(f'assets/figures/{image}')
        self.pos = pos
        self.first_move = first_move
        self.pov = pov
        #self.selected = selected
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (self.pov[pos][0], self.pov[pos][1])
    def get_rect(self):
        return self.image_rect
        

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

        self.white_pov = {
                        'A8': (68, 71), 'B8': (147, 71), 'C8': (226, 71), 'D8': (305, 71), 'E8': (384, 71), 'F8': (461, 71), 'G8': (539, 71), 'H8': (619, 71),  
                        'A7': (68, 150), 'B7': (147, 150), 'C7': (226, 150), 'D7': (305, 150), 'E7': (384, 150), 'F7': (461, 150), 'G7': (539, 150), 'H7': (619, 150), 
                        'A6': (68, 229), 'B6': (147, 229), 'C6': (226, 229), 'D6': (305, 229), 'E6': (384, 229), 'F6': (461, 229), 'G6': (539, 229), 'H6': (619, 229), 
                        'A5': (68, 308), 'B5': (147, 308), 'C5': (226, 308), 'D5': (305, 308), 'E5': (384, 308), 'F5': (461, 308), 'G5': (539, 308), 'H5': (619, 308), 
                        'A4': (68, 387), 'B4': (147, 387), 'C4': (226, 387), 'D4': (305, 387), 'E4': (384, 387), 'F4': (461, 387), 'G4': (539, 387), 'H4': (619, 387), 
                        'A3': (68, 464), 'B3': (147, 464), 'C3': (226, 464), 'D3': (305, 464), 'E3': (384, 464), 'F3': (461, 464), 'G3': (539, 464), 'H3': (619, 464), 
                        'A2': (68, 543), 'B2': (147, 543), 'C2': (226, 543), 'D2': (305, 543), 'E2': (384, 543), 'F2': (461, 543), 'G2': (539, 543), 'H2': (619, 543), 
                        'A1': (68, 622), 'B1': (147, 622), 'C1': (226, 622), 'D1': (305, 622), 'E1': (384, 622), 'F1': (461, 622), 'G1': (539, 622), 'H1': (619, 622)
                        }

        self.pov = self.white_pov

        #  Keys

        self.RETURN = False
        self.ESC = False

        self.selected = None

        # Colors

        self.WHITE = (255, 255, 255)

        #  Load assets

        self.BOARD = pygame.image.load('assets/board.jpg')
        self.RED_SQUARE = pygame.image.load('assets/red_square.png')

        #  Black

        self.black_pawn = pygame.image.load('assets/figures/black_pawn.png')

        #  White
        
        self.white_pawn_1 = Figure('p', True, 'white_pawn.png', 'A2', True, self.pov)
        self.white_pawn_2 = Figure('p', True, 'white_pawn.png', 'B2', True, self.pov)
        self.white_pawn_3 = Figure('p', True, 'white_pawn.png', 'C2', True, self.pov)
        self.white_pawn_4 = Figure('p', True, 'white_pawn.png', 'D2', True, self.pov)
        self.white_pawn_5 = Figure('p', True, 'white_pawn.png', 'E2', True, self.pov)
        self.white_pawn_6 = Figure('p', True, 'white_pawn.png', 'F2', True, self.pov)
        self.white_pawn_7 = Figure('p', True, 'white_pawn.png', 'G2', True, self.pov)
        self.white_pawn_8 = Figure('p', True, 'white_pawn.png', 'H2', True, self.pov)
        self.white_knight_1 = Figure('k', True, 'white_knight.png', 'B1', False, self.pov)
        self.white_knight_2 = Figure('k', True, 'white_knight.png', 'G1', False, self.pov)
        self.white_bishop_1 = Figure('b', True, 'white_bishop.png', 'C1', False, self.pov)
        self.white_bishop_2 = Figure('b', True, 'white_bishop.png', 'F1', False, self.pov)
        self.white_rook_1 = Figure('r', True, 'white_rook.png', 'A1', False, self.pov)
        self.white_rook_2 = Figure('r', True, 'white_rook.png', 'H1', False, self.pov)
        self.white_king = Figure('K', True, 'white_king.png', 'E1', False, self.pov)
        self.white_queen = Figure('q', True, 'white_queen.png', 'D1', False, self.pov)

        self.figures = [self.white_pawn_1, self.white_pawn_2, self.white_pawn_3,
                        self.white_pawn_4, self.white_pawn_5, self.white_pawn_6,
                        self.white_pawn_7, self.white_pawn_8, self.white_knight_1,
                        self.white_knight_2, self.white_bishop_1, self.white_bishop_2,
                        self.white_rook_1, self.white_rook_2, self.white_king,
                        self.white_queen]

        #  Apply all assets and variables

        pygame.display.set_caption('Chess game')   


    def start_game(self):

        while self.run_game:
            self.check_input()
            self.check_event()

            self.display.blit(self.BOARD, (0, 0))
            

            #  Draw sprites of figures
            
            for figure in self.figures:
                self.draw_sprite(figure.image, self.pov[figure.pos][0], self.pov[figure.pos][1])

            if not self.selected  is None:
                self.draw_sprite(self.RED_SQUARE, self.pov[self.selected.pos][0], self.pov[self.selected.pos][1])

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
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for figure in self.figures:
                    if figure.get_rect().collidepoint(pos):
                        self.selected = figure
                        return

    def check_event(self):
        if self.ESC:
            self.run_game = False
            self.curr_menu.run_menu = True

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
