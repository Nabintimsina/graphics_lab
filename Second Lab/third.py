import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 800
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
        screen.set_at((round(x), round(y)), BLACK)
        x = x+ xinc
        y = y + yinc
        



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear the screen 
        screen.fill(WHITE)
        
        # draw line
        LineDraw(200, 200, 600, 200)
        LineDraw(200, 600, 600, 600)
        LineDraw(200, 200, 200, 600)
        # LineDraw(600, 200, 600, 600)
        LineDraw(600, 200, 600, 300)
        
        LineDraw(200, 200, 200, 600)
        LineDraw(200, 200, 400, 0)
        LineDraw(600, 200, 400, 0)
        LineDraw(200, 300, 600, 300)
        
        
        LineDraw(200, 300, 300, 400)
        LineDraw(300, 400, 700, 400)
        LineDraw(600, 300, 700, 400)
        
        
        LineDraw(300, 400, 300, 700)
        LineDraw(700, 400, 700, 700)
        
        # update the scren 
        pygame.display.flip()
        

if __name__ == "__main__" :
    main()