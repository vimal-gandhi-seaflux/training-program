def ractangle():
    i=0
    while(i<=2):
        print("@" * 2 )    
        i+=1
    
def square():
    i=0
    while(i<=2):
        print("&" * 4 )    
        i+=1
def triangle():
        rows = 3

        k = 0

        for i in range(1, 4):
            for space in range(1, (4-i)+1):
                print(end="  ")
        
            while k!=(2*i-1):
                print("* ", end="")
                k += 1
        
            k = 0
            print()

a= 'a'
while(a != 'q'):
    a=input("enter which shape you want to print:ractangle,square,triangle or you want to quite than press q:")
    if('square'==a): 
        square()
    elif('ractangle'==a):
        ractangle()
    
    elif('triangle'==a):
        triangle()
    elif(a=='q'):
        break
