import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DDA LINE DRAWING ALGORITHM")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def LineDraw(x1, y1, x2, y2):
    
    dx = x2 - x1
    dy = y2- y1
    steps = max(abs(dx), abs(dy))
    
    xinc = dx/steps
    yinc = dy/steps
    
    x = x1 
    y= y1
    
    i = 0
    for i in range(steps):
        i= i+1
        screen.set_at((round(x), round(y)), WHITE)
        x = x+ xinc
        y = y + yinc
        



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear the screen 
        screen.fill(BLACK)
        
        # draw line
        LineDraw(100, 100,700, 500)
        
        # update the scren 
        pygame.display.flip()
        

if __name__ == "__main__" :
    main()