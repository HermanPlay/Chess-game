import pygame


class Menu:
    def __init__(self):
        pass

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):

        self.game = game
    
    def display_menu(self):
        self.run_menu = True

        while self.run_menu:
            self.game.check_input()
            self.check_event()

            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Start', 50, self.game.WIDTH//2, self.game.HEIGHT//2)

            self.blit_screen()
            
    def check_event(self):
        if self.game.RETURN:
            self.run_menu = False
            self.game.run_game = True
            print('Wyszedlem z menu')
        if self.game.ESC:
            self.run_menu = False
            self.game.run_app = False
            self.game.run_game = False
