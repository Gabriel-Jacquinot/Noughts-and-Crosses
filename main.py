import pygame
from menu.menu import create_menu, draw_text

pygame.init() # This just makes all the functions you call work properly by initialsing them

# Variables for window
WIDTH, HEIGHT = 800, 600 # The width and height that the display will be set to
logo = pygame.image.load("logo.png") # Loading the named image file and assigning it to a variable
menu_logo = pygame.transform.smoothscale(logo, (768, 768))

# Setting up the window
window = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialising the display as window, with a width and height
pygame.display.set_caption("Noughts and Crosses") # Name of the program (Top left when run)
pygame.display.set_icon(menu_logo) # This puts the logo image in the top left

# Variables
clock = pygame.time.Clock() # Getting the current time so a tick rate can be set later (for game FPS)
fps = 60
font = pygame.font.SysFont("Calbri", 70)

# Making everything
window.fill((52, 78, 91)) # Background colour of the program
play_local_button, play_computer_button, quit_button = create_menu(window, WIDTH, HEIGHT)
draw_text(window, "Noughts and Crosses", font, "white", ((WIDTH / 2) - ((40 * 25) / 2) / 2), ((HEIGHT /2 ) - (260))) 

run = True # So that game is always playing on program startup
while run is True: # This is the game loop, so anything that happens here will undergo the 60 frames a second refresh rate. Without the game loop nothing would happen as nothing is updated so the program would just got to pygame.quit() at the end

    pos_x, pos_y = pygame.mouse.get_pos() # Assigning the active position of the users mouse under x and y variables
    pos = pygame.mouse.get_pos() # Mouse positions under one variable for ease of use later
    for events in pygame.event.get(): # This is where the program is checking for any changes that are made by the user such as keyboard and mouse inputs
        if events.type == pygame.QUIT: # Checking for a click on the top right exit button (the cross on the window)
            run = False # Ends the game loop and thefore the program
        if events.type == pygame.MOUSEBUTTONDOWN: # Checking for any mouse clicks at all
            if quit_button.rect.collidepoint(pos): # Checking if this click is on the quit button or not by matching it to mouse coordinates
                run = False # Ends the game loop and thefore the program
            if play_local_button.rect.collidepoint(pos):
                print("Loading Local Game...")
            if play_computer_button.rect.collidepoint(pos):
                print("Loading Computer Game...")
                
    play_computer_button.button_hover(pos)                   
    play_local_button.button_hover(pos)
    quit_button.button_hover(pos)
    
    play_computer_button.make_button(window)
    play_local_button.make_button(window)
    quit_button.make_button(window)
                  
    pygame.display.update() # This is constantly refreshing the game during the loop to make any changes or else the display would not update
    
    clock.tick(fps) # Establishing the tick rate or fps of the game
    
pygame.quit() # Quits the game; this line is reached when the game loop is False