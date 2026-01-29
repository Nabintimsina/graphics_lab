import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BLA LINE DRAWING ALGORITHM")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

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
            

def Translate(x1,y1, x2,y2, tx, ty):
    
    x1 += tx
    y1 += ty
    x2 += tx
    y2 += ty
    
    
    return (x1, y1, x2, y2)
          
def Scale(x1,y1, x2,y2, sx, sy):
    
    x1 =  sx* x1
    y1 = sy * y1
    x2 = sx * x2
    y2 = sy * y2

    return (x1, y1, x2, y2)


def Rotate(x1,y1, x2,y2, dtheta):
    
    theta = math.radians(dtheta)
    
    x1 = x1*math.cos(theta) - y1*math.sin(theta)
    x2 = x2*math.cos(theta) - y2*math.sin(theta)
    
    y1 = x1*math.sin(theta) + y1*math.cos(theta)
    y2 = x2*math.sin(theta) + y2*math.cos(theta)
    
    print(x1, y1, x2, y2)
    
    return (x1, y1, x2, y2)


def ReflectionX(x1,y1, x2,y2,):
    
    

    
    

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # clear the screen 
        screen.fill(WHITE)
        
        x1 = 100
        y1 = 200
        x2 = 300
        y2 = 350
        tx = 50
        ty = 50
        sx = 2
        sy = 1
        theta = -30
        
        # draw line
        LineDraw(x1, y1, x2, y2, 'black')
        
        (xt1, yt1, xt2, yt2) = Translate(x1, y1, x2, y2, tx, ty)
        (xs1, ys1, xs2, ys2) = Scale(x1, y1, x2, y2, sx, sy)
        (xr1, yr1, xr2, yr2) = Rotate(x1, y1, x2, y2, theta)
        
        LineDraw(xt1,yt1, xt2, yt2, 'green')
        LineDraw(xs1,ys1, xs2, ys2, 'red')
        LineDraw(xr1, yr1, xr2, yr2, 'blue')
       
        
        
        
        # update the scren 
        pygame.display.flip()
        

if __name__ == "__main__" :
    main()