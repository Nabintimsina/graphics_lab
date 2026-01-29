import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLA LINE DRAWING ALGORITHM")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pivot = 450

def LineDraw(x1, y1, x2, y2, color):
    
    dx = round(abs(x2 - x1))
    dy = round(abs(y2- y1))
    
    if(x2>x1):
        lx = 1
    else:
        lx = -1
    
    if(y2>y1):
        ly = 1
        
    else:
        ly= -1
        
    x = x1 
    y= y1
    
    screen.set_at((round(x),round(y)), color)
    
    
    if(dx> dy):
        
        p = 2*dy- dx
        
        
        for i in range(dx):
            if(p<0):
                x = x+lx
                y = y
                p = p+ 2*dy 
            
            else:
                x = x+lx
                y = y+ly
                p = p+ 2*dy - 2*dx
                
            screen.set_at((round(x),round(y)), color)
                
    else:
        p = 2*dx- dy
        
        
        for _ in range(dy):
            if(p<0):
                x = x
                y = y+ly
                p = p+ 2*dx
            
            else:
                x = x+lx
                y = y+ly
                p = p+ 2*dx - 2*dy
                
            screen.set_at((round(x),round(y)), color)
            


def Reflection(x1,y1, x2,y2,axis):
    
    xc = 450
    yc = 450
    
    if(axis == 'y') :
    
        x1 -= xc
        x2 -= xc

    if(axis == 'x'):

        y1 += yc
        y2 += yc
    
    
    
    
    return (x1, y1, x2, y2)
    
    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear the screen 
        screen.fill(WHITE)
        
        x1 = 200+ pivot
        y1 = 200
        x2 = 300+pivot
        y2 = 330

        
        # draw line
        LineDraw(450 ,0 ,450, 900, 'black')
        LineDraw(0 ,450, 900,450, 'black')
        LineDraw(x1,  y1,x2, y2, 'black')
       
        (xR1, yR1, xR2, yR2) = Reflection(x1, y1, x2, y2, 'y')
        
        LineDraw(xR1, yR1, xR2, yR2, 'blue')
        
        (xR1, yR1, xR2, yR2) = Reflection(x1, y1, x2, y2, 'x')
        
        LineDraw(xR1, yR1, xR2, yR2, 'red')

       
        
        
        
        # update the scren 
        pygame.display.flip()
        

if __name__ == "__main__" :
    main()