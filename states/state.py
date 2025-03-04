class State():
    def __init__(self, main):
        self.menu = main
        self.previous = None
        
    def update(self, delta_time, actions):
        pass
    
    def render(self, window):
        pass
    
    def enter(self):
        if len(self.main.state_stack) > 1:
            self.previous = self.main.state_stack[-1]
        self.main.state_stack.append(self)
        
    def exit(self):
        self.main.state_stack.pop()