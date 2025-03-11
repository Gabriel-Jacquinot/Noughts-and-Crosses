import pygame

class Image:
    def __init__(self, file, x, y, size):
        self.file = pygame.Surface.convert_alpha(file)
        self.x = x
        self.y = y
        self.size = size
        
    def make_image(self, window):
        window.blit(self.file, (self.x, self.y))