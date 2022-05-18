from game import Game


def main():
    
    game = Game()

    while game.run_app:
        game.curr_menu.display_menu()  # Start menu loop, in which current menu is displayed
        game.start_game()  # Start game loop, which basically starts the game



if __name__ == "__main__":
    main()