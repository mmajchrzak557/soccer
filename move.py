import pygame
import math
import numpy as np
import os

def find_point_in_array(array, pos):
    for i in range(array.shape[0]):
        if array[i, 1].y != pos[1]:
            continue
        else:
            for j in range(array.shape[1]):
                if array[i, j].x == pos[0]:
                    return array[i, j]
    return None
            
def round_to_nearest(value, target):
    return int(value + target/2 - (value + target/2) % target)

class Move:
    def __init__(self, x, y, sc, points, turn):
        self.start = (round_to_nearest(x, sc), round_to_nearest(y, sc))
        self.pos = self.start
        self.steps = [self.pos]
        find_point_in_array(points, self.start).visited = True
        self.done = False
        self.color = (255, 200, 200) if turn else (200, 200, 255)
        self.ball = pygame.image.load(os.getcwd() + '\\ball.png')
        self.ball = pygame.transform.scale(self.ball, (26, 26))
    
    def show(self, window, sc, field):
        mouse_pos = pygame.mouse.get_pos()
        new_x = round_to_nearest(mouse_pos[0], sc) 
        new_y = round_to_nearest(mouse_pos[1], sc) 
        point = (new_x, new_y)
        if self.point_in_field(point, field.rects):
            pygame.draw.circle(window, (200, 150, 150), point, 4)
        #pygame.draw.circle(window, (0, 0, 0), self.pos, 4)
        if len(self.steps) > 1:
            for i in range(1, len(self.steps)):
                pygame.draw.line(window, self.color, self.steps[i - 1], self.steps[i], 4)
        window.blit(self.ball, (self.pos[0] - 13, self.pos[1] - 13))
        
    def make(self, window, mouse_pos, sc, field):
        x = round_to_nearest(mouse_pos[0], sc)
        y = round_to_nearest(mouse_pos[1], sc)
        prev_x = self.pos[0]
        prev_y = self.pos[1]
        
        if x == prev_x and y == prev_y: return
        
        line_length = math.sqrt((prev_x - x)**2 + (prev_y - y)**2)

        if line_length > 1.5*sc: return
                
        start_point = find_point_in_array(field.points, (prev_x, prev_y))
        end_point   = find_point_in_array(field.points, (x, y))
        
        
        if end_point == None: return
        if not end_point.visited: self.done = True
        if not self.point_in_field((end_point.x, end_point.y), field.rects): return
        
        lon   = np.sign(x - prev_x)
        lat   = np.sign(y - prev_y) 
        
        lat_dict = {-1:'S', 0:'', 1:'N'}
        lon_dict = {-1:'E', 0:'', 1:'W'}
        
        move_dir     = lat_dict[lat]  + lon_dict[lon]
        move_dir_rev = lat_dict[-lat] + lon_dict[-lon]
        
        if start_point.wall and end_point.wall and len(move_dir) < 2: return
        if start_point.wall and end_point.ptype == 3 : return
        
        if end_point.moves[move_dir]:
            self.pos = (x, y)
            self.steps.append(self.pos)
            end_point.moves[move_dir]       = False
            start_point.moves[move_dir_rev] = False
            end_point.visited = True
            
    def point_in_field(self, point, field_rects):
        for rect in field_rects:
            if rect.collidepoint(point): return True
        return False

        

        
        