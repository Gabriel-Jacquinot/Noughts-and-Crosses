from states.state import State

class LocalGame(State):
    def __init__(self, main):
        State.__init__(self, main)
    
    def update(self, delta_time, actions):
        self.main.reset_keys()
        
    def render(self, window):
        window = 
    