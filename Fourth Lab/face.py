import pygame
import sys

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Midpoint Circle DRAWING ALGORITHM")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def printCirclePoints(xc, yc, x, y):
    
        screen.set_at((xc+x,yc+y), BLACK)
        screen.set_at((xc-x,yc-y), BLACK)
        screen.set_at((xc+x,yc-y), BLACK)
        screen.set_at((xc-x,yc+y), BLACK)
        
        screen.set_at((xc+y,yc+x), BLACK)
        screen.set_at((xc-y,yc-x), BLACK)
        screen.set_at((xc+y,yc-x), BLACK)
        screen.set_at((xc-y,yc+x), BLACK)

def printSemiPoints(xc, yc, x, y):
    
        screen.set_at((xc+x,yc+y), BLACK)
        # screen.set_at((xc-x,yc-y), BLACK)
        # screen.set_at((xc+x,yc-y), BLACK)
        
        screen.set_at((xc-x,yc+y), BLACK)
        
        screen.set_at((xc+y,yc+x), BLACK)
        
        # screen.set_at((xc-y,yc-x), BLACK)
        # screen.set_at((xc+y,yc-x), BLACK)
        
        screen.set_at((xc-y,yc+x), BLACK)

        


def drawCircle(xc, yc, r, semi = False):
    
    x = 0
    y= r
    
    p = 1-r
    
    while (y>x):
        
        if(p<0):
            x= x+1
            p = p+ 2*x+1
         
        else:
            x = x+1
            y= y-1
            p= p+2*x - 2*y +1
            
        
        if(semi == False):
            printCirclePoints(xc, yc, x, y)
        
        else:
            printSemiPoints(xc, yc, x, y)
        
        
        



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
        drawCircle(200,200,20)
        drawCircle(400,200,20)
        drawCircle(300,300,150, True)
        
        # update the scren 
        pygame.display.flip()
        

if __name__ == "__main__" :
    main()