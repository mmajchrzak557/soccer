import pygame
import sys
from field import Field
from move import Move

class Game:
    def __init__(self):
        pygame.init()
        w = 10
        h = 16
        sc = 35
        window_width  = (w + 2) * sc
        window_height = (h + 2) * sc
        self.window = pygame.display.set_mode((window_width, window_height))
        self.clock = pygame.time.Clock()        
        self.field = Field(w, h, sc)
        self.move = Move(int(w*sc/2 + sc), int(h*sc/2 + sc), sc)
        
    def run(self):
        while(True):
            self.clock.tick(30)

            events = pygame.event.get()
            
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.move.make(self.window, pygame.mouse.get_pos(), 35, self.field.points)
                    
            self.window.fill((255, 255,255))       
            self.field.show(self.window)
            self.move.show(self.window, 35, self.field)
            pygame.display.update()
            
game = Game()
game.run()
                
                
            
        
        
