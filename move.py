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
        self.steps = [self.pos]
    
    def show(self, window, sc, field):
        mouse_pos = pygame.mouse.get_pos()
        new_x = round_to_nearest(mouse_pos[0], sc) 
        new_y = round_to_nearest(mouse_pos[1], sc) 
        point = (new_x, new_y)
        for rect in field.rects:
            if rect.collidepoint(point):
                pygame.draw.circle(window, (200, 150, 150), point, 4)
        pygame.draw.circle(window, (0, 0, 0), self.pos, 4)
        if len(self.steps) > 1:
            for i in range(1, len(self.steps)):
                pygame.draw.line(window, (255, 200, 200), self.steps[i - 1], self.steps[i], 4)
        
    def make(self, window, mouse_pos, sc, points):
        x = round_to_nearest(mouse_pos[0], sc)
        y = round_to_nearest(mouse_pos[1], sc)
        prev_x = self.pos[0]
        prev_y = self.pos[1]
        
        if x == prev_x and y == prev_y: return
        
        line_length = math.sqrt((prev_x - x)**2 + (prev_y - y)**2)

        if line_length > 1.5*sc: return
                
        start_point = find_point_in_array(points, (prev_x, prev_y))
        end_point   = find_point_in_array(points, (x, y))
        
        lon   = np.sign(x - prev_x)
        lat   = np.sign(y - prev_y) 
        
        lat_dict = {-1:'S', 0:'', 1:'N'}
        lon_dict = {-1:'E', 0:'', 1:'W'}
        
        move_dir     = lat_dict[lat] + lon_dict[lon]
        move_dir_rev = lat_dict[-lat] + lon_dict[-lon]
        if end_point.moves[move_dir]:
            self.pos = (x, y)
            self.steps.append(self.pos)
            end_point.moves[move_dir]       = False
            start_point.moves[move_dir_rev] = False
        

        
        