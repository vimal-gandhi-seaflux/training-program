import random


def guess():
    print("enter a and binteger in between you want a guess the number:")
    a=int(input("select number 1 :"))
    b=int(input("select number 2 :"))
    s=random.randint(a,b)
    i=1
    while(i<=5):
        guess_number=int(input(f"enter your {i} guess number : "))
        if(guess_number==s):
            print("YOU WIN!!!")
            exit()
        elif(guess_number>s):
            print("you select too high number ")
        elif(guess_number<s):
            print("you select too low number")
        i+=1
    print("you guess limit is over")


guess()