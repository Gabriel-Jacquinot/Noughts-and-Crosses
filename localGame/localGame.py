import pygame
import sys
from menu.buttons import Button

class GameLocal:
    def __init__(self, window, gameStateManager):
        self.window = window
        self.gameStateManager = gameStateManager

        # Initialize game variables
        self.is_running = True # Renamed from `run` to `is_running`
        self.click = False
        self.end_game = False
        self.draw = False
        self.winner = 0
        self.p1_score = 0
        self.p2_score = 0
        self.total = 0
        self.position = []
        self.spaces = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 'p1' # p1 = first player (crosses)
        self.p1_clicked = False
        self.p2_clicked = True
        self.cross = pygame.image.load('White_Cross.png')
        pygame.Surface.convert_alpha(self.cross)
        self.nought = pygame.image.load('White_Nought.png')
        pygame.Surface.convert_alpha(self.nought)

        # Font
        pygame.font.init()
        self.font = pygame.font.SysFont('Verdana', 36)
        
        self.bg = (112, 137, 156)

        # Grid rectangles
        self.topleft = pygame.Rect(100, 100, 200, 200)
        self.topmid = pygame.Rect(300, 100, 200, 200)
        self.topright = pygame.Rect(500, 100, 200, 200)
        self.midleft = pygame.Rect(100, 300, 200, 200)
        self.mid = pygame.Rect(300, 300, 200, 200)
        self.midright = pygame.Rect(500, 300, 200, 200)
        self.botleft = pygame.Rect(100, 500, 200, 200)
        self.botmid = pygame.Rect(300, 500, 200, 200)
        self.botright = pygame.Rect(500, 500, 200, 200)

        # Button rectangles
        self.reset_button = pygame.Rect(800, 480, 350, 160) # Reset Game button
        self.menu_button = pygame.Rect(800, 160, 350, 160) # Return to Menu button
        self.quit_button = pygame.Rect(920, 370, 112, 60)

    def grid(self):
        grid_lines = (255, 255, 255)
        self.window.fill(self.bg)
        pygame.draw.rect(self.window, (80, 103, 120), [0, 0, 1200, 800], width=10)
        for x in range(1, 3):
            # Vertical lines
            pygame.draw.line(self.window, grid_lines, (300, 700), (300, 100), width=3)
            pygame.draw.line(self.window, grid_lines, (500, 700), (500, 100), width=3)
            # Horizontal lines
            pygame.draw.line(self.window, grid_lines, (100, 300), (700, 300), width=3)
            pygame.draw.line(self.window, grid_lines, (100, 500), (700, 500), width=3)

    def check_winner(self):
        y_pos = 0
        for x in self.spaces:
            # Columns
            if sum(x) == 3:
                self.winner = '1'
                self.end_game = True
            if sum(x) == -3:
                self.winner = '2'
                self.end_game = True

            # Rows
            if self.spaces[0][y_pos] + self.spaces[1][y_pos] + self.spaces[2][y_pos] == 3:
                self.winner = '1'
                self.end_game = True
            if self.spaces[0][y_pos] + self.spaces[1][y_pos] + self.spaces[2][y_pos] == -3:
                self.winner = '2'
                self.end_game = True
            y_pos += 1

        # Diagonal
        if self.spaces[0][0] + self.spaces[1][1] + self.spaces[2][2] == 3 or self.spaces[2][0] + self.spaces[1][1] + self.spaces[0][2] == 3:
            self.winner = '1'
            self.end_game = True
        if self.spaces[0][0] + self.spaces[1][1] + self.spaces[2][2] == -3 or self.spaces[2][0] + self.spaces[1][1] + self.spaces[0][2] == -3:
            self.winner = '2'
            self.end_game = True
            
        self.check_spaces = [[abs(num) for num in row] for row in self.spaces]
        self.total = sum(sum(row) for row in self.check_spaces)
        if self.total == 9:
            self.draw = True
            self.check_spaces = 0

    def win_screen(self):
        self.total = 0
        self.check_spaces = 0
        win_text = 'Player ' + str(self.winner) + ' Wins!'
        win_img = self.font.render(win_text, True, (255, 255, 255))
        pygame.draw.rect(self.window, (151, 164, 186), [200, 200, 400, 400], border_radius=15)
        pygame.draw.rect(self.window, (80, 103, 120), [200, 200, 400, 400], width=10, border_radius=15)
        self.window.blit(win_img, (283, 375))
        
    def draw_screen(self):
        self.total = 0
        self.check_spaces = 0
        self.draw = False
        win_text = "Draw"
        win_img = self.font.render(win_text, True, (255, 255, 255))
        pygame.draw.rect(self.window, (151, 164, 186), [200, 200, 400, 400], border_radius=15)
        pygame.draw.rect(self.window, (80, 103, 120), [200, 200, 400, 400], width=10, border_radius=15)
        self.window.blit(win_img, (350, 375))

    def buttons(self):
        # Reset Game button
        pygame.draw.rect(self.window, (255, 255, 255), self.reset_button, width=10, border_radius=35)
        reset_text = ' Reset Game'
        reset_img = self.font.render(reset_text, True, (255, 255, 255))
        self.window.blit(reset_img, (self.reset_button.x + 50, self.reset_button.y + 60))

        # Return to Menu button
        pygame.draw.rect(self.window, (255, 255, 255), self.menu_button, width=10, border_radius=35)
        menu_text = 'Return to Menu'
        menu_img = self.font.render(menu_text, True, (255, 255, 255))
        self.window.blit(menu_img, (self.menu_button.x + 30, self.menu_button.y + 60))
    
    def draw_text(self):
        font = pygame.font.SysFont('Verdana', 40)
        colour = (255, 255, 255)
        x = 825
        y = 60
        if self.turn == "p1":
            pygame.draw.rect(self.window, self.bg, (x, y, 300, 100))
            text = "Turn : Player 1"
            img = font.render(text, True, pygame.Color(colour))
            self.window.blit(img, (x, y))
        elif self.turn == "p2":
            pygame.draw.rect(self.window, self.bg, (x, y, 300, 100))
            text = "Turn : Player 2"
            img = font.render(text, True, pygame.Color(colour))
            self.window.blit(img, (x, y))
        
    def hover_buttons(self):
        pos = pygame.mouse.get_pos()
        quit_button = Button("Calbri", 60, False, "Quit", True, (112, 137, 156), "white", 920, 370, 112, 60, "red", hoverColour = (80, 103, 120))
        quit_button.button_hover(pos)
        quit_button.make_button(self.window)
        
    def play_again(self):
        self.spaces = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 'p1'
        self.p1_clicked = False
        self.p2_clicked = True
        self.end_game = False
        self.draw = False
        self.total = 0
        self.check_spaces = 0
        self.winner = 0
        self.grid()
        self.buttons()
        self.score()
        
    def score(self):
        pygame.draw.rect(self.window, self.bg, (150, 30, 570, 50))
        if self.winner == "1":
            self.p1_score += 1
        elif self.winner == "2":
            self.p2_score += 1
            
        font = pygame.font.SysFont('Verdana', 40)
        
        text = f"Player 1 : {self.p1_score}"
        img = font.render(text, True, pygame.Color(255, 255, 255))
        self.window.blit(img, (110, 30))
        
        text = f"Player 2 : {self.p2_score}"
        img = font.render(text, True, pygame.Color(255, 255, 255))
        self.window.blit(img, (460, 30))

    def handle_click(self, pos):
        if not self.end_game and not self.draw:
            if self.turn == 'p1':
                if self.topleft.collidepoint(pos) and self.spaces[0][0] == 0:
                    pygame.Surface.blit(self.window, self.nought, (110, 110))
                    self.spaces[0][0] = 1
                    self.turn = 'p2'
                elif self.topmid.collidepoint(pos) and self.spaces[0][1] == 0:
                    pygame.Surface.blit(self.window, self.nought, (310, 110))
                    self.spaces[0][1] = 1
                    self.turn = 'p2'
                elif self.topright.collidepoint(pos) and self.spaces[0][2] == 0:
                    pygame.Surface.blit(self.window, self.nought, (510, 110))
                    self.spaces[0][2] = 1
                    self.turn = 'p2'
                elif self.midleft.collidepoint(pos) and self.spaces[1][0] == 0:
                    pygame.Surface.blit(self.window, self.nought, (110, 310))
                    self.spaces[1][0] = 1
                    self.turn = 'p2'
                elif self.mid.collidepoint(pos) and self.spaces[1][1] == 0:
                    pygame.Surface.blit(self.window, self.nought, (310, 310))
                    self.spaces[1][1] = 1
                    self.turn = 'p2'
                elif self.midright.collidepoint(pos) and self.spaces[1][2] == 0:
                    pygame.Surface.blit(self.window, self.nought, (510, 310))
                    self.spaces[1][2] = 1
                    self.turn = 'p2'
                elif self.botleft.collidepoint(pos) and self.spaces[2][0] == 0:
                    pygame.Surface.blit(self.window, self.nought, (110, 510))
                    self.spaces[2][0] = 1
                    self.turn = 'p2'
                elif self.botmid.collidepoint(pos) and self.spaces[2][1] == 0:
                    pygame.Surface.blit(self.window, self.nought, (310, 510))
                    self.spaces[2][1] = 1
                    self.turn = 'p2'
                elif self.botright.collidepoint(pos) and self.spaces[2][2] == 0:
                    pygame.Surface.blit(self.window, self.nought, (510, 510))
                    self.spaces[2][2] = 1
                    self.turn = 'p2'
                self.draw_text()
                    
            elif self.turn == 'p2':
                if self.topleft.collidepoint(pos) and self.spaces[0][0] == 0:
                    pygame.Surface.blit(self.window, self.cross, (110, 110))
                    self.spaces[0][0] = -1
                    self.turn = 'p1'
                elif self.topmid.collidepoint(pos) and self.spaces[0][1] == 0:
                    pygame.Surface.blit(self.window, self.cross, (310, 110))
                    self.spaces[0][1] = -1
                    self.turn = 'p1'
                elif self.topright.collidepoint(pos) and self.spaces[0][2] == 0:
                    pygame.Surface.blit(self.window, self.cross, (510, 110))
                    self.spaces[0][2] = -1
                    self.turn = 'p1'
                elif self.midleft.collidepoint(pos) and self.spaces[1][0] == 0:
                    pygame.Surface.blit(self.window, self.cross, (110, 310))
                    self.spaces[1][0] = -1
                    self.turn = 'p1'
                elif self.mid.collidepoint(pos) and self.spaces[1][1] == 0:
                    pygame.Surface.blit(self.window, self.cross, (310, 310))
                    self.spaces[1][1] = -1
                    self.turn = 'p1'
                elif self.midright.collidepoint(pos) and self.spaces[1][2] == 0:
                    pygame.Surface.blit(self.window, self.cross, (510, 310))
                    self.spaces[1][2] = -1
                    self.turn = 'p1'
                elif self.botleft.collidepoint(pos) and self.spaces[2][0] == 0:
                    pygame.Surface.blit(self.window, self.cross, (110, 510))
                    self.spaces[2][0] = -1
                    self.turn = 'p1'
                elif self.botmid.collidepoint(pos) and self.spaces[2][1] == 0:
                    pygame.Surface.blit(self.window, self.cross, (310, 510))
                    self.spaces[2][1] = -1
                    self.turn = 'p1'
                elif self.botright.collidepoint(pos) and self.spaces[2][2] == 0:
                    pygame.Surface.blit(self.window, self.cross, (510, 510))
                    self.spaces[2][2] = -1
                    self.turn = 'p1'
                self.draw_text()
            
            self.check_winner()
            if self.end_game:
                self.total = 0
                self.check_spaces = 0
                self.score()
                self.win_screen()
            elif self.draw:
                self.check_spaces = 0
                self.total = 0
                self.score()
                self.draw_screen()

        # Handle button clicks
        if self.reset_button.collidepoint(pos):
            self.play_again()
            self.draw_text()
        elif self.menu_button.collidepoint(pos):
            self.gameStateManager.set_state("menu") # Return to menu
            self.is_running = False  # Stop the game loop
        elif self.quit_button.collidepoint(pos): # Checking if this click is on the quit button or not by matching it to mouse coordinates
            pygame.quit()
            exit()

    def run(self):
        self.grid()
        self.buttons()
        self.draw_text()
        self.score()
        while self.is_running:
            self.hover_buttons()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and not self.click:
                    self.click = True
                    self.handle_click(event.pos)
                elif event.type == pygame.MOUSEBUTTONUP and self.click:
                    self.click = False

            pygame.display.update()