def printPoints(x, y, xc , yc):
    
    print(f"{xc+x}, {yc +y}")
    print(f"{xc-x}, {yc -y}")    
    print(f"{xc+x}, {yc-y}")
    print(f"{xc-x}, {yc +y}")
    
    print()
    
    

def drawEllipse(xc, yc, rx,ry):
    x= 0
    y = ry
    rx2 = pow(rx, 2)
    ry2 = pow(ry, 2)
    
    printPoints(x,y, xc, yc)
    
    p = ry2 - rx2*ry + rx2/4
    while (2*rx2*y > 2*ry2*x):

        if p< 0:
            x = x+1
            y = y
            p = p+ 2*ry2*x+ry2
            
        else:
            x = x+1
            y = y-1
            p = p+ 2*ry2*x+ry2-2*rx2*y
        
        printPoints(x,y, xc, yc)
        
    
    
    p = ry2* pow((x+1/2), 2)+ rx2* pow((y- 1), 2) - ry2*rx2 
    while (y>0):

        
        if p> 0:
            x = x
            y = y-1
            p = p-2*rx2 * y + rx2
            
        else:
            
            x = x+1
            y = y-1
            p = p-2*rx2 * y + rx2 + 2*ry2*x
            
        printPoints(x,y, xc, yc) 
            
            
drawEllipse(0,0, 4, 6)