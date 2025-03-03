import pygame # Getting all the functions that come with the pygame library, without this the pygame functions we use would not work
from .buttons import Button

def create_menu(window, WIDTH, HEIGHT):
    # Buttons which can be made and their properties
    play_computer = Button("Calbri", 60, False, "Play vs Computer", True, (50, 50, 50), "white", ((WIDTH/ 2) - (380/ 2)), ((HEIGHT/ 2) - (190/ 2)) - 33, 380, 60, "white", hoverColour = (0, 0, 0)) # change the last two numbers for the button length and width and the two numbers before for x, y position from the top left corner
    play_local = Button("Calbri", 60, False, "Play vs Friend", True, (50, 50, 50), "white", ((WIDTH/ 2) - (310/ 2)), ((HEIGHT/ 2) - (60/ 2)) - 30, 310, 60, "white", hoverColour = (0, 0, 0)) # change the last two numbers for the button length and width and the two numbers before for x, y position from the top left corner
    quit_button = Button("Calbri", 60, False, "Quit", True, (50, 50, 50), "white", ((WIDTH/ 2) - (112/ 2)), ((HEIGHT/ 2) + (75/ 2)) - 28, 112, 60, "red", hoverColour = (0, 0, 0))
    
    # Making the buttons
    quit_button.make_button(window) # Actually making the button now and putting it on the window
    play_local.make_button(window)
    play_computer.make_button(window)
    
    return play_local, play_computer, quit_button

def draw_text(window, text, font, colour, x, y):
    img = font.render(text, True, pygame.Color(colour))
    pygame.draw.rect(window, (0, 139, 139), (0, 0, window.get_width(), 120))
    window.blit(img, (x, y))