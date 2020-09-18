import numpy as np
from point import Point
import pygame


class Field:
    def __init__(self, w, h, sc):
        self.points = self.get_points_array(w, h, sc)
        self.lines  = self.get_lines()
        self.rects  = self.get_rects(w, h, sc)
    
    def get_numpy_array(self, w, h):
        if w % 2 != 0 or h % 2 != 0:            
            w -= 1
            h -= 1
            print('Field size changed, dimensions must be even numbers')
            
        l = int(w/2 - 1)
        
        array = np.zeros((int(h/2), int(w/2)))
        goal_insert    = [0] * l + [3]
        top_insert     = [3] + [2] * (l - 1) + [3]
        side_insert    = [2] + [1] * l
        
        array[0]  = np.array(goal_insert)
        array[1]  = np.array(top_insert)
        array[2:] = np.array(side_insert)
        
        middle_horizontal = np.array(side_insert)[np.newaxis]
        flipped = np.flip(array, 0)
        array = np.concatenate((array, middle_horizontal, flipped), axis=0)
        
        middle_vertical = [2] + [1] * (h - 1) + [2]
        middle_vertical = np.array(middle_vertical).reshape((h + 1), 1)
        flipped = np.flip(array, 1)
        array = np.concatenate((array, middle_vertical, flipped), axis=1)
        return array
    
    def get_points_array(self, w, h, sc):
        base_array = self.get_numpy_array(w, h)
        new_array = np.empty(base_array.shape, dtype=object)
        rows = base_array.shape[0]
        cols = base_array.shape[1]
        for i in range(rows):
            row_condition = i == 1 or i == 0 or i == rows - 2 or i == rows - 1
            for j in range(cols):
                col_condition = j == 0 or j == cols - 1
                wall = True if row_condition or col_condition else False
                element = base_array[i, j]
                new_array[i, j] = Point(j * sc + sc, i * sc + sc, element, wall)
        new_array[1, cols//2].wall = False
        new_array[rows - 2, cols//2].wall = False
        return new_array
    
    def get_lines(self):
        lines = []
        for i in range(self.points.shape[0]):
            for j in range(self.points.shape[1]):
                point = self.points[i, j]
                if point.ptype == 3:
                    lines.append((point.x, point.y))
        
        for i in range(self.points.shape[1]):
            for j in range(self.points.shape[0]):
                point = self.points[j, i]
                if point.ptype == 3:
                    lines.append((point.x, point.y))
        return lines
    
    def get_rects(self, w, h, sc):        
        l = int((w - 2)/2)
        left = (l + 1)*sc
        main = pygame.Rect((sc, sc*2, w*sc + 1, (h - 2)*sc + 1))
        top_goal = pygame.Rect((left, sc, 2*sc + 1, sc + 1))
        bottom_goal = pygame.Rect((left, h*sc, 2*sc + 1, sc + 1))
        return [main, top_goal, bottom_goal]
                
    def show(self, window):
        for i in range(self.points.shape[0]):
            for j in range(self.points.shape[1]):
                if self.points[i, j].ptype == 1:
                    self.points[i, j].show(window)
                    
        for i in range(0, len(self.lines), 2):
            start_pos = (self.lines[i][0], self.lines[i][1])
            end_pos   = (self.lines[i + 1][0], self.lines[i + 1][1])
            pygame.draw.line(window, (0, 0, 0), start_pos, end_pos, 3)
        

