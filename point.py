import pygame

class Point:
    def __init__(self, x, y, point_type, wall):
        self.x = x
        self.y = y
        self.ptype = point_type
        self.moves = {'N':True, 'NE':True, 'E':True, 'SE':True,
                      'S':True,'SW':True, 'W':True, 'NW':True}
        self.wall = wall
        self.visited = wall
    
    def show(self, window):
        if self.ptype == 0:
            pass
        elif self.ptype == 1:
            pygame.draw.circle(window, (30, 100, 30), (self.x, self.y), 2)
        elif self.ptype == 2:
            pygame.draw.circle(window, (100, 30, 30), (self.x, self.y), 3)
        else:
            pygame.draw.circle(window, (130, 50, 50), (self.x, self.y), 4)
    


            
        
        