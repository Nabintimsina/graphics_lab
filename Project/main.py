import pygame
import sys
import small_circle as 

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle DRAWING ALGORITHM")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def printPoints(xc, yc, x, y):
    
        screen.set_at((xc+x,yc+y), BLACK)
        screen.set_at((xc-x,yc-y), BLACK)
        screen.set_at((xc+x,yc-y), BLACK)
        screen.set_at((xc-x,yc+y), BLACK)
        
        screen.set_at((xc+y,yc+x), BLACK)
        screen.set_at((xc-y,yc-x), BLACK)
        screen.set_at((xc+y,yc-x), BLACK)
        screen.set_at((xc-y,yc+x), BLACK)

        


def drawCircle(xc, yc, r):
    
    x = 0
    y= r
    
    p = 1-r
    
    while (y>x):
        
        if(p<0):
            x= x+1
            p = p+ 2*x+1
         
        else:
            x = x+1
            # y= y-1
            p= p+2*x - 2*y +1
            
        
        printPoints(xc, yc, x, y)
        



def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear the screen 
        screen.fill(WHITE)
        
        # draw circle
        drawCircle(300,300,250)
        
        # update the scren 
        pygame.display.flip()
        

if __name__ == "__main__" :
    main()