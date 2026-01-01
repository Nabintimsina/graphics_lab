def printPoints(xc, yc, x, y):
    
        print(f"({xc+x}, {yc+y})")
        print(f"({xc-x}, {yc-y})")
        print(f"({xc-x}, {yc+y})")
        print(f"({xc+x}, {yc-y})")
        print(f"({xc+y}, {yc+x})")
        print(f"({xc-y}, {yc-x})")
        print(f"({xc+y}, {yc-x})")
        print(f"({xc-y}, {yc+x})")
        
        print()
        




def drawCircle(xc, yc, r):
    
    x = 0
    y= r
    
    p = 1-r
    
    while (y>x):
        
        if(p<0):
            x= x+1
            y = y
            p = p+ 2*x+1
         
        else:
            x = x+1
            y= y-1
            p= p+2*x - 2*y +1
            
        
        printPoints(xc, yc, x, y)

        
                          
        
    
def main():
    drawCircle(20, 10, 6)
        
       
if __name__ == "__main__" :
    main()