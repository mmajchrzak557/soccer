import pygame

def round_to_nearest(value, target):
    return int(value + target/2 - (value + target/2) % target)

class Move:
    def __init__(self, x, y):
        self.start = (x, y)
    
    def display_moves(self, window, sc):
        mouse_pos = pygame.mouse.get_pos()
        new_x = round_to_nearest(mouse_pos[0], sc) 
        new_y = round_to_nearest(mouse_pos[1], sc) 
        pygame.draw.circle(window, (200, 150, 150), (new_x, new_y), 4)
        
        