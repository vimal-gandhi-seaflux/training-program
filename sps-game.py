import random
def sps_game():
        n=1
        u=0
        while(n< 10):   
            s=random.choice(['stone','paper','sissor'])  
            a=input("enter your choice from these: Stone , Paper ,Sissor :")
            f=open('sps-game.txt','a')
            if((a == 'stone') or (a== 'paper') or (a== 'sissor')):
                if(s==a):
                    print("YOU WIN !!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: you win \n ")
                    f.close()
                    u+=1
                elif(s!=a):
                    print("you fail!!!")
                    f.write(f"round-no:{n}   user choice:{a} system choice:{s}  winner of round: computer win \n ")
                    f.close()
                n+=1
            else:
                print("check input")
        print(f"you win {u} times")
sps_game()
