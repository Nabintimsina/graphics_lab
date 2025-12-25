
def LineDraw(x1, y1, x2, y2):
    
    dx = abs(x2 - x1)
    dy = abs(y2- y1)
    
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
    
    print(f"({x}, {y})")
    
    
    if(dx> dy):
        
        p = 2*dy- dx
        
        k= 0
        
        for i in range(dx):
            if(p<0):
                x = x+lx
                y = y
                p = p+ 2*dy 
            
            else:
                x = x+lx
                y = y+ly
                p = p+ 2*dy - 2*dx
                
            print(f"({x}, {y})")
                
    else:
        p = 2*dx- dy
        
        k= 0
        
        for i in range(dy):
            if(p<0):
                x = x
                y = y+ly
                p = p+ 2*dx
            
            else:
                x = x+lx
                y = y+ly
                p = p+ 2*dx - 2*dy
                
            print(f"({x}, {y})")
        
          
            
        



def main():
    LineDraw(1, 2,12, 7)
        
       
if __name__ == "__main__" :
    main()