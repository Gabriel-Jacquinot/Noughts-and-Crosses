import pygame # Getting all the functions that come with the pygame library, without this the pygame functions we use would not work

pygame.init() # This just makes all the functions you call work properly by initialsing them

WIDTH, HEIGHT = 800, 600 # The width and height that the display will be set to
logo = pygame.image.load("icons8-tic-tac-toe-67.png") # Loading the named image file and assigning it to a variable
menu_logo = pygame.transform.smoothscale(logo, (768, 768))

window = pygame.display.set_mode((WIDTH, HEIGHT)) # Initialising the display as window, with a width and height
pygame.display.set_caption("Noughts and Crosses") # Name of the program (Top left when run)
pygame.display.set_icon(menu_logo) # This puts the logo image in the top left

clock = pygame.time.Clock() # Getting the current time so a tick rate can be set later (for game FPS)
fps = 60

font = pygame.font.SysFont("Calbri", 70)

def draw_text(text, font, colour, x, y):
    img = font.render(text, True, colour)
    pygame.draw.rect(window, (0, 139, 139), (0, 0, WIDTH, 120))
    window.blit(img, (x, y))

class button: # Making a class for any button that gets made so that you can very easily make multiple by just inputing the properties you want it to have
    def __init__(self, font, size, boolean1, text, boolean2, bgColour, textColour, posx, posy, length, width, borderColour): # This is a placeholder which will be different for each button, enter a set of values for each variable to make a button
        self.font = pygame.font.SysFont(font, int(size), bool(boolean1)) # Setting a font for the button
        self.textColour = pygame.Color(textColour) # Setting a text colour
        self.text = self.font.render(text, bool(boolean2), pygame.Color(textColour)) # Set the text for the button and its colour
        self.rect = pygame.Rect(int(posx), int(posy), int(length), int(width)) # Draw the clickable button which is a rectangle (pygame.Rect)
        self.colour = pygame.Color(bgColour) # The background colour of the button
        self.borderColour = borderColour

    def make_button(self, window): # The __init__ function is just establishing the variables in terms of pygame and this function actually makes a new buton using those
        pygame.draw.rect(window, self.colour, self.rect) # Draw the outside rectangle which the clickable rectanlge will be inside
        pygame.draw.rect(window, self.borderColour, self.rect, width = 3)
        window.blit(self.text, (self.rect.x + 10, self.rect.y + 10)) # This is where both the clickable button rectangle and the actual text and background rectangle are combined into one object
 
    window.fill((52, 78, 91)) # Background colour of the program

# Buttons which can be made and their properties
playLocal = ["Calbri", 60, False, "Play a Friend", True, "black", "white", ((WIDTH/ 2) - (285/ 2)), ((HEIGHT/ 2) - (95)) - 50, 285, 60, "white"] # change the last two numbers for the button length and width and the two numbers before for x, y position from the top left corner
playLocalButton = button(*playLocal) # Sending all of the values (*) into the button class to make a new button
playComputer = ["Calbri", 60, False, "Play the Computer", True, "black", "white", ((WIDTH/ 2) - (400/ 2)), ((HEIGHT/ 2) - (60/ 2)) - 50, 395, 60, "white"] # change the last two numbers for the button length and width and the two numbers before for x, y position from the top left corner
playComputerButton = button(*playComputer) # Sending all of the values (*) into the button class to make a new button
quit = ["Calbri", 60, False, "Quit", True, "black", "white", ((WIDTH/ 2) - (112/ 2)), ((HEIGHT/ 2) + (70/ 2)) - 50, 112, 60, "red"] 
quitButton = button(*quit)

# Making the buttons
quitButton.make_button(window) # Actually making the button now and putting it on the window
playLocalButton.make_button(window)
playComputerButton.make_button(window)

draw_text("Noughts and Crosses", font, "white", ((WIDTH / 2) - ((40 * 25) / 2) / 2), ((HEIGHT /2 ) - (260))) 
 
run = True # So that game is always playing on program startup
while run is True: # This is the game loop, so anything that happens here will undergo the 60 frames a second refresh rate. Without the game loop nothing would happen as nothing is updated so the program would just got to pygame.quit() at the end

    pos_x, pos_y = pygame.mouse.get_pos() # Assigning the active position of the users mouse under x and y variables
    pos = pygame.mouse.get_pos() # Mouse positions under one variable for ease of use later
    for events in pygame.event.get(): # This is where the program is checking for any changes that are made by the user such as keyboard and mouse inputs
        if events.type == pygame.QUIT: # Checking for a click on the top right exit button (the cross on the window)
            run = False # Ends the game loop and thefore the program
        if events.type == pygame.MOUSEBUTTONDOWN: # Checking for any mouse clicks at all
            if quitButton.rect.collidepoint(pos): # Checking if this click is on the quit button or not by matching it to mouse coordinates
                run = False # Ends the game loop and thefore the program
            if playLocalButton.rect.collidepoint(pos):
                print("Loading Game...")
                print("Work in progress")
            
    pygame.display.update() # This is constantly refreshing the game during the loop to make any changes or else the display would not update
    
    clock.tick(fps) # Establishing the tick rate or fps of the game
    
pygame.quit() # Quits the game; this line is reached when the game loop is False
