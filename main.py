import pygame
from states.gameStateManager import GameStateManager
from menu.menu import Menu
from localGame.localGame import GameLocal
from computerGame.computerGame import GameComp

pygame.init()

# Properties for the window
WIDTH, HEIGHT = 1200, 800
logo = pygame.image.load("logo.png")
menu_logo = pygame.transform.smoothscale(logo, (768, 768))
FPS = 60

class Program:
    def __init__(self):
        # Setting up the window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT)) # Initializing the display as window with a width and height
        pygame.display.set_caption("Noughts and Crosses")
        pygame.display.set_icon(menu_logo)

        # Variables
        self.clock = pygame.time.Clock() # Getting the current time so a tick rate can be set later (for game FPS)
        self.gameStateManager = GameStateManager("menu") # The default state when the program is first run if the menu

        # Creating the Menu
        self.menu = Menu(self.window, self.gameStateManager, WIDTH, HEIGHT)
        
        # Initialize GameLocal and GameComp
        self.game_local = GameLocal(self.window, self.gameStateManager)
        self.game_comp = GameComp(self.window, self.gameStateManager)

    def run(self):
        while True: # Main game loop
            current_state = self.gameStateManager.get_state() # Get the current game state

            # Reinitialize GameLocal if switching back to "play_local"
            if current_state == "play_local" and self.game_local is None:
                self.game_local = GameLocal(self.window, self.gameStateManager)
            elif current_state != "play_local":
                self.game_local = None # Reset GameLocal when not in "play_local" state

            # Reinitialize GameComp if switching back to "play_comp"
            if current_state == "play_comp" and self.game_comp is None:
                self.game_comp = GameComp(self.window, self.gameStateManager)
            elif current_state != "play_comp":
                self.game_comp = None # Reset GameComp when not in "play_comp" state

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if current_state == "menu":
                        self.menu.handle_click(event.pos) # Handle clicks in the menu
                    elif current_state == "play_comp" and self.game_comp is not None:
                        self.game_comp.handle_click(event.pos) # Handle clicks in the computer game
                    elif current_state == "play_local" and self.game_local is not None:
                        self.game_local.handle_click(event.pos) # Handle clicks in the local game

            # Run the appropriate state
            if current_state == "menu":
                self.menu.run()
            elif current_state == "play_local" and self.game_local is not None:
                self.game_local.run() # Run the local game
            elif current_state == "play_comp" and self.game_comp is not None:
                self.game_comp.run(self.window, WIDTH, HEIGHT) # Run the computer game

            pygame.display.update() # Update the display
            self.clock.tick(FPS)

if __name__ == "__main__":
    program = Program()
    program.run()