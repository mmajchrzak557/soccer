import pygame
import sys
from field import Field
from move import Move

def map_val(n, start1, stop1, start2, stop2):
  return int(((n-start1)/(stop1-start1))*(stop2-start2)+start2)


class Game:
    def __init__(self):
        pygame.init()
        w = 8
        h = 12
        scale = 50
        self.h = h
        self.sc = scale
        window_width  = (w + 2) * scale
        window_height = (h + 2) * scale
        self.window = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()        
        self.field = Field(w, h, scale)
        start_x = int(w*self.sc/2 + self.sc)
        start_y = int(h*self.sc/2 + self.sc)
        self.turn = False
        self.move = Move(start_x, start_y, self.sc, self.field.points, self.turn)
        self.lines = []
        
        
    def run(self):
        while(True):
            self.clock.tick(30)

            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.move.make(self.window, pygame.mouse.get_pos(), self.sc, self.field)
                    if self.move.done:
                        self.lines += self.move.steps
                        self.turn = not self.turn
                        self.move = Move(self.move.pos[0], self.move.pos[1],
                                         self.sc, self.field.points, self.turn)
                        
            pos = self.move.pos[1]
            color = map_val(pos, self.sc, self.h*self.sc + self.sc, 0, 250)
            
            self.window.fill((color, 255, 255 - color))       
            self.field.show(self.window)
            
            if len(self.lines) > 1:
                for i in range(1, len(self.lines)):
                   pygame.draw.line(self.window, (0, 0, 0), self.lines[i - 1], self.lines[i], 4) 
            self.move.show(self.window, self.sc, self.field)
            pygame.display.update()
            
Game().run()
                
                
            
        
        
