import pygame
from menu.buttons import Button

class GameComp:
    def __init__(self, window, gameStateManager):
       self.window = window
       self.gameStateManager = gameStateManager
       
    def run(self, window, WIDTH, HEIGHT): 
        self.window.fill((112, 137, 156))
        pos = pygame.mouse.get_pos()
        
        font = pygame.font.SysFont("Calibri", 52)
        text = "Opponent : Computer"
        colour = "white"
        x, y = (WIDTH / 2) - 225, 35

        pygame.draw.rect(window, (80, 103, 120), [0, 0, 1200, 800], width = 10)

        img = font.render(text, True, pygame.Color(colour))
        window.blit(img, (x, y))

        self.menu_button = Button("Calbri", 60, False, "Menu", True, (112, 137, 156), "white", 15, 30, 132, 60, "white", hoverColour = (80, 103, 120))
        self.quit_button = Button("Calbri", 60, False, "Quit", True, (112, 137, 156), "white", WIDTH - 135, 30, 112, 60, "red", hoverColour = (80, 103, 120))
        
        self.quit_button.button_hover(pos)
        self.menu_button.button_hover(pos)
        
        self.quit_button.make_button(window)
        self.menu_button.make_button(window)
        
        # Making the grid properties
        pygame.draw.rect(window, (0, 139, 139), ((WIDTH / 2) - (450 / 2), (HEIGHT / 2) - 140, 450, 400))
        # for i in range(2):
        #     pygame.draw.line(window, (255, 255, 255), ((WIDTH / 2) - (450 / 2)), (((HEIGHT / 2) - 140) / 3))
        
    def handle_click(self, pos):
        if self.quit_button.rect.collidepoint(pos): # Checking if this click is on the quit button or not by matching it to mouse coordinates
            pygame.quit()
            exit()
        elif self.menu_button.rect.collidepoint(pos):
            self.gameStateManager.set_state("menu")