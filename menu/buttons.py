import pygame

class Button: # Making a class for any button that gets made so that you can very easily make multiple by just inputing the properties you want it to have
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

