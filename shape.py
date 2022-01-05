def ractangle():
    for i in range(1, 5) :
        for j in range(1,20):
            if (i==1 or i==4 or j==1 or j==19):
                print("*",end="")
            else:
                print(end=" ")
        print()
   
def square():
    for i in range(1,5):
        for j in range(1,5):
            if (i==1 or i==4 or j==1 or j==4):
                print("*",end="")
            else:
                print(end=" ")
        print()
    
def triangle():
    for i in range(1,5):
    
        for s in range(1,5-i):
            print(end=" ")
        for j in range(i) :
            print("*",end=" ")
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
