import pygame
from states.gameStateManager import GameStateManager
from menu.menu import Menu
from localGame.localGame import GameLocal
from computerGame.computerGame import GameComp

pygame.init() # This just makes all the functions you call work properly by initialsing them

# Variables for window
WIDTH, HEIGHT = 800, 600 # The width and height that the display will be set to
logo = pygame.image.load("logo.png") # Loading the named image file and assigning it to a variable5
menu_logo = pygame.transform.smoothscale(logo, (768, 768))
FPS = 60

class Program:
    def __init__(self):
        
        # Setting up the window
        self.window = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialising the display as window, with a width and height
        pygame.display.set_caption("Noughts and Crosses") # Name of the program (Top left when run)
        pygame.display.set_icon(menu_logo) # This puts the logo image in the top left

        # Variables
        self.clock = pygame.time.Clock() # Getting the current time so a tick rate can be set later (for game FPS)
        
        self.gameStateManager = GameStateManager("menu") 

        # Creating the Menu
        self.menu = Menu(self.window, self.gameStateManager)
        
        self.game_local = GameLocal(self.window, self.gameStateManager)
        
        self.game_comp = GameComp(self.window, self.gameStateManager)
        
    def run(self):
        while True: # This is the game loop, so anything that happens here will undergo the 60 frames a second refresh rate. Without the game loop nothing would happen as nothing is updated so the program would just got to pygame.quit() at the end
            current_state = self.gameStateManager.get_state()

            for event in pygame.event.get(): # This is where the program is checking for any changes that are made by the user such as keyboard and mouse inputs
                if event.type == pygame.QUIT: # Checking for a click on the top right exit button (the cross on the window)
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN: # Checking for any mouse clicks at all
                    if current_state == "menu":
                        self.menu.handle_click(event.pos)
                    if current_state == "play_comp":
                        self.game_comp.handle_click(event.pos)
                    if current_state == "play_local":
                        self.game_local.handle_click(event.pos)
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        print("Loading Menu")
                        self.gameStateManager.set_state("menu")
                    
            if current_state == "menu":
                self.menu.run()
            elif current_state == "play_local":
                self.game_local.run(self.window, WIDTH, HEIGHT)
            elif current_state == "play_comp":
                self.game_comp.run(self.window, WIDTH, HEIGHT)
                
            # Add other calls for game aspects like playing the computer here #
                        
            pygame.display.update() # This is constantly refreshing the game during the loop to make any changes or else the display would not update
            self.clock.tick(FPS) # Establishing the tick rate or fps of the game
    
if __name__ == "__main__":
    program = Program()
    program.run()