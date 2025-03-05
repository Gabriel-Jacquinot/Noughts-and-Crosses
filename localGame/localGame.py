class GameLocal:
    def __init__(self, window, gameStateManager):
       self.window = window
       self.gameStateManager = gameStateManager
       
    def run(self): 
        self.window.fill("red")
                