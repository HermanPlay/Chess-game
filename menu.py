class Menu:
    def __init__(self):
        pass

    def blit_screen(self):
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):

        self.game = game
        self.run_menu = True
    
    def display_menu(self):
        

        while self.run_menu:
            self.game.check_input()
            self.check_event()
            self.blit_screen()
            
    def check_event(self):
        if self.game.RETURN:
            self.run_menu = False
            print('Wyszedlem z menu')
