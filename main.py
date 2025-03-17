import pygame
from states.gameStateManager import GameStateManager
from menu.menu import Menu
from localGame.localGame import GameLocal
from computerGame.computerGame import GameComp

pygame.init()  # Initialize Pygame

# Variables for window
WIDTH, HEIGHT = 1200, 800  # The width and height that the display will be set to
logo = pygame.image.load("logo.png")  # Loading the named image file and assigning it to a variable
menu_logo = pygame.transform.smoothscale(logo, (768, 768))
FPS = 60

class Program:
    def __init__(self):
        # Setting up the window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))  # Initializing the display as window, with a width and height
        pygame.display.set_caption("Noughts and Crosses")  # Name of the program (Top left when run)
        pygame.display.set_icon(menu_logo)  # This puts the logo image in the top left

        # Variables
        self.clock = pygame.time.Clock()  # Getting the current time so a tick rate can be set later (for game FPS)
        self.gameStateManager = GameStateManager("menu")  # Initialize the game state manager with the "menu" state

        # Creating the Menu
        self.menu = Menu(self.window, self.gameStateManager, WIDTH, HEIGHT)
        
<<<<<<< HEAD
        # Initialize GameLocal and GameComp
        self.game_local = None
        self.game_comp = None
=======
        self.game_local = GameLocal(self.window, self.gameStateManager)
        
        self.game_comp = GameComp(self.window, self.gameStateManager)
        5
    def run(self):
        while True: # This is the game loop, so anything that happens here will undergo the 60 frames a second refresh rate. Without the game loop nothing would happen as nothing is updated so the program would just got to pygame.quit() at the end
            current_state = self.gameStateManager.get_state()
>>>>>>> origin

    def run(self):
        while True:  # Main game loop
            current_state = self.gameStateManager.get_state()  # Get the current game state

            # Reinitialize GameLocal if switching back to "play_local"
            if current_state == "play_local" and self.game_local is None:
                self.game_local = GameLocal(self.window, self.gameStateManager)
            elif current_state != "play_local":
                self.game_local = None  # Reset GameLocal when not in "play_local" state

            # Reinitialize GameComp if switching back to "play_comp"
            if current_state == "play_comp" and self.game_comp is None:
                self.game_comp = GameComp(self.window, self.gameStateManager)
            elif current_state != "play_comp":
                self.game_comp = None  # Reset GameComp when not in "play_comp" state

            for event in pygame.event.get():  # Handle events
                if event.type == pygame.QUIT:  # Check for the window close event
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse clicks
                    if current_state == "menu":
                        self.menu.handle_click(event.pos)  # Handle clicks in the menu
                    elif current_state == "play_comp" and self.game_comp is not None:
                        self.game_comp.handle_click(event.pos)  # Handle clicks in the computer game
                    elif current_state == "play_local" and self.game_local is not None:
                        self.game_local.handle_click(event.pos)  # Handle clicks in the local game
                if event.type == pygame.KEYDOWN:  # Check for key presses
                    if event.key == pygame.K_ESCAPE:  # Return to menu on ESC key
                        self.gameStateManager.set_state("menu")

            # Run the appropriate state
            if current_state == "menu":
                self.menu.run()
            elif current_state == "play_local" and self.game_local is not None:
                self.game_local.run()  # Run the local game
            elif current_state == "play_comp" and self.game_comp is not None:
                self.game_comp.run(self.window, WIDTH, HEIGHT)  # Run the computer game

            pygame.display.update()  # Update the display
            self.clock.tick(FPS)  # Maintain the FPS

if __name__ == "__main__":
    program = Program()
    program.run()