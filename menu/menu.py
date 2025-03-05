import pygame # Getting all the functions that come with the pygame library, without this the pygame functions we use would not work
from .buttons import Button

def create_menu(window, WIDTH, HEIGHT):
    # Buttons which can be made and their properties
    play_computer = Button("Calbri", 60, False, "Play vs Computer", True, (90, 90, 90), "white", ((WIDTH/ 2) - (380/ 2)), ((HEIGHT/ 2) - (190/ 2)) - 34, 380, 60, "white", hoverColour = (30, 30, 30)) # change the last two numbers for the button length and width and the two numbers before for x, y position from the top left corner
    play_local = Button("Calbri", 60, False, "Play vs Friend", True, (90, 90, 90), "white", ((WIDTH/ 2) - (310/ 2)), ((HEIGHT/ 2) - (60/ 2)) - 30, 310, 60, "white", hoverColour = (30, 30, 30)) # change the last two numbers for the button length and width and the two numbers before for x, y position from the top left corner
    quit_button = Button("Calbri", 60, False, "Quit", True, (90, 90, 90), "white", ((WIDTH/ 2) - (112/ 2)), ((HEIGHT/ 2) + (75/ 2)) - 28, 112, 60, "red", hoverColour = (30, 30, 30))
    
    # Making the buttons
    quit_button.make_button(window) # Actually making the button now and putting it on the window
    play_local.make_button(window)
    play_computer.make_button(window)
    
    return play_local, play_computer, quit_button

def draw_text(window, text, font, colour, x, y):
    img = font.render(text, True, pygame.Color(colour))
    pygame.draw.rect(window, (0, 139, 139), (0, 0, window.get_width(), 120))
    window.blit(img, (x, y))

class Menu:
    def __init__(self, window, gameStateManager):
        self.window = window
        self.gameStateManager = gameStateManager

    def run(self):
        font = pygame.font.SysFont("Calibri", 70)

        self.window.fill((52, 78, 91)) # Background colour of the program
        self.play_local_button, self.play_computer_button, self.quit_button = create_menu(self.window, 800, 600)
        
        draw_text(self.window, "Noughts and Crosses", font, "white", (800 / 2) - (47 * 25 / 2) / 2, (600 // 2) - 260)
        
        # Get mouse position
        pos = pygame.mouse.get_pos()

        # Update hover effect for buttons
        self.play_local_button.button_hover(pos)
        self.play_computer_button.button_hover(pos)
        self.quit_button.button_hover(pos)

        # Redraw buttons with hover effect
        self.play_local_button.make_button(self.window)
        self.play_computer_button.make_button(self.window)
        self.quit_button.make_button(self.window)
        
    def handle_click(self, pos):
        if self.quit_button.rect.collidepoint(pos): # Checking if this click is on the quit button or not by matching it to mouse coordinates
            pygame.quit()
            exit()
        elif self.play_local_button.rect.collidepoint(pos):
            print("Loading Local Game...")
            self.gameStateManager.set_state("play_local")
        elif self.play_computer_button.rect.collidepoint(pos):
            print("Loading Computer Game...")
            self.gameStateManager.set_state("play_comp")
