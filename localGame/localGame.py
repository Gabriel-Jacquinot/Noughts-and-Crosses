import pygame
from menu.buttons import Button

class GameLocal:
    def __init__(self, window, gameStateManager):
       self.window = window
       self.gameStateManager = gameStateManager
       
    def run(self, window, WIDTH, HEIGHT): 
        self.window.fill((52, 78, 91))
        pos = pygame.mouse.get_pos()
        
        font = pygame.font.SysFont("Calibri", 52)
        text = "Opponent : Player 2" # Make this switch for each new move
        colour = "white"
        x, y = (WIDTH / 2) - 210, 35

        img = font.render(text, True, pygame.Color(colour))
        pygame.draw.rect(window, (0, 139, 139), (0, 0, window.get_width(), 120))
        window.blit(img, (x, y))

        self.menu_button = Button("Calbri", 60, False, "Menu", True, (50, 50, 50), "white", 15, 30, 132, 60, "white", hoverColour = (10, 10, 10))
        self.quit_button = Button("Calbri", 60, False, "Quit", True, (50, 50, 50), "white", WIDTH - 135, 30, 112, 60, "red", hoverColour = (10, 10, 10))
        
        self.quit_button.button_hover(pos)
        self.menu_button.button_hover(pos)
        
        self.quit_button.make_button(window)
        self.menu_button.make_button(window)
        
    def handle_click(self, pos):
        if self.quit_button.rect.collidepoint(pos): # Checking if this click is on the quit button or not by matching it to mouse coordinates
            pygame.quit()
            exit()
        elif self.menu_button.rect.collidepoint(pos):
            self.gameStateManager.set_state("menu")