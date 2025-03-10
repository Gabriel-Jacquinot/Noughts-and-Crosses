import pygame

class Image:
    def __init__(self, file, x, y, size):
        self.file = pygame.transform.scale(pygame.image.load(file), size)
        self.x = x
        self.y = y
        self.size = size
        
    def make_image(self, window):
        window.blit(self.file, (self.x, self.y))