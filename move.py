import pygame
import math
import numpy as np

def find_point_in_array(array, pos):
    for i in range(array.shape[0]):
        if array[i, 1].y != pos[1]:
            continue
        else:
            for j in range(array.shape[1]):
                if array[i, j].x == pos[0]:
                    return array[i, j]
    print('Could not find given point')
    return None
            
def round_to_nearest(value, target):
    return int(value + target/2 - (value + target/2) % target)

class Move:
    def __init__(self, x, y, sc):
        self.start = (round_to_nearest(x, sc), round_to_nearest(y, sc))
        self.pos = (x, y)
        self.next_pos = None
    
    def show(self, window, sc, field):
        mouse_pos = pygame.mouse.get_pos()
        new_x = round_to_nearest(mouse_pos[0], sc) 
        new_y = round_to_nearest(mouse_pos[1], sc) 
        point = (new_x, new_y)
        for rect in field.rects:
            if rect.collidepoint(point):
                pygame.draw.circle(window, (200, 150, 150), point, 4)
        pygame.draw.circle(window, (0, 0, 0), self.pos, 4)
        if self.next_pos != None:
            pygame.draw.line(window, (255, 200, 200), self.pos, self.next_pos, 4)
        
    def make(self, window, mouse_pos, sc, points):
        x1 = round_to_nearest(mouse_pos[0], sc)
        y1 = round_to_nearest(mouse_pos[1], sc)
        x2 = self.pos[0]
        y2 = self.pos[1]
        line_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        if line_length > 1.5*sc:
            return
        
        point = find_point_in_array(points, (x1, y1))
        
        horizontal = np.sign(x1 - x2)
        vertical   = np.sign(y1 - y2)      
        directions = {-1:'S', 0:'', 1:'N'}
        s1 = directions[vertical]
        directions = {-1:'E', 0:'', 1:'W'}
        s2 = directions[horizontal]
        if s1 + s2 == '':
            return
        
        if point.moves[s1 + s2]:
            self.next_pos = self.pos
            self.pos = (x1, y1)
            point.moves[s1 + s2] = False
            print(s1 + s2)
            print(point.moves[s1 + s2])
            print(point.moves)
        

        
        