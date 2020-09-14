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
        self.move = Move(100, 100)
        
    def run(self):
        while(True):
            self.clock.tick(30)
            keys = pygame.key.get_pressed()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.window.fill((255, 255,255))       
            self.field.show(self.window)
            self.move.display_moves(self.window, 35)
            pygame.display.update()
            
game = Game()
game.run()
                
                
            
        
        
