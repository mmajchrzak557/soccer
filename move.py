import pygame

def round_to_nearest(value, target):
    return int(value + target/2 - (value + target/2) % target)

class Move:
    def __init__(self, x, y, sc):
        self.start = (round_to_nearest(x, sc), round_to_nearest(y, sc))
        self.pos = (x, y)
        self.next_pos = None
    
    def display_moves(self, window, sc):
        mouse_pos = pygame.mouse.get_pos()
        new_x = round_to_nearest(mouse_pos[0], sc) 
        new_y = round_to_nearest(mouse_pos[1], sc) 
        pygame.draw.circle(window, (200, 150, 150), (new_x, new_y), 4)
        
    def show_ball(self, window):
        pygame.draw.circle(window, (0, 0, 0), self.pos, 4)
        if self.next_pos != None:
            pygame.draw.line(window, (255, 200, 200), self.pos, self.next_pos, 4)
        
    def make(self, window, mouse_pos, sc):
        x = round_to_nearest(mouse_pos[0], sc)
        y = round_to_nearest(mouse_pos[1], sc)
        self.next_pos = (x, y)
        print(self.pos, mouse_pos)
        
        