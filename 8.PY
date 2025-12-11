def myfun():
    n= int(input("enter a number "))
    rev = 0
    temp = n

    while(n != 0):
        rem = n%10
        rev = rev*10+rem
        # n = int(n/10)
        n = n//10
    
    if(rev == temp):
        print("Palindrome")
    
    else :
        print("not ")
        
        

myfun()