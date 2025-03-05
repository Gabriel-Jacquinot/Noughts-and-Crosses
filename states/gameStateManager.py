class GameStateManager:
    def __init__(self, initial_state):
        self.current_state = initial_state
    
    def get_state(self):
        return self.current_state
    
    def set_state(self, state):
        print(f"State changing from {self.current_state} to {state}")
        self.current_state = state