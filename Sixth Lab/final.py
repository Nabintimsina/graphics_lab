import pygame
import sys
import math

pygame.init()
WIDTH, HEIGHT = 900, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Transformations")



def to_screen(x, y):
    sx = WIDTH // 2 + int(x)    
    sy = HEIGHT // 2 - int(y)    
    return (sx, sy)

def LineDraw(x1, y1, x2, y2, color):
    x1, y1 = to_screen(x1, y1)
    x2, y2 = to_screen(x2, y2)

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    lx = 1 if x2 > x1 else -1
    ly = 1 if y2 > y1 else -1

    x, y = x1, y1
    screen.set_at((x, y), color)

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx):
            x += lx
            if p >= 0:
                y += ly
                p -= 2 * dx
            p += 2 * dy
            screen.set_at((x, y), color)
    else:
        p = 2 * dx - dy
        for _ in range(dy):
            y += ly
            if p >= 0:
                x += lx
                p -= 2 * dy
            p += 2 * dx
            screen.set_at((x, y), color)

def Translate(x1, y1, x2, y2, tx, ty):
    LineDraw(x1+tx, y1+ty, x2+tx, y2+ty, 'red')

def Scale(x1, y1, x2, y2, sx, sy):
    LineDraw(x1*sx, y1*sy, x2*sx, y2*sy, 'blue')

def Rotate(x1, y1, x2, y2, angle):
    theta = math.radians(angle)
    xr1 = x1*math.cos(theta) - y1*math.sin(theta)
    yr1 = x1*math.sin(theta) + y1*math.cos(theta)
    xr2 = x2*math.cos(theta) - y2*math.sin(theta)
    yr2 = x2*math.sin(theta) + y2*math.cos(theta)
    LineDraw(xr1, yr1, xr2, yr2, 'green')

def ReflectX(x1, y1, x2, y2):
    LineDraw(x1, -y1, x2, -y2, 'purple')

def ReflectY(x1, y1, x2, y2):
    LineDraw(-x1, y1, -x2, y2, 'orange')

def draw_axes():
    LineDraw(-WIDTH//2, 0, WIDTH//2, 0, 'black')  
    LineDraw(0, HEIGHT//2, 0, -HEIGHT//2, 'black')


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill('white')
        draw_axes()

        x1, y1 = 100, 80
        x2, y2 = 200, 200

        LineDraw(x1, y1, x2, y2, 'black')

        Translate(x1, y1, x2, y2, 60, 40) 
        Rotate(x1, y1, x2, y2, -30)       
        ReflectX(x1, y1, x2, y2)            
        ReflectY(x1, y1, x2, y2)
        Scale(x1, y1, x2, y2, 2, 1.5)       

        pygame.display.flip()

if __name__ == "__main__":
    main()
