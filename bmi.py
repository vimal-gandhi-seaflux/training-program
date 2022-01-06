def bmi():
    try :
                name = input("Enter Your Name:-")
                weight = int(input("Enter Your Weight in kg :"))
                height = int(input("Enter Your Height in cm :"))
                bmi_cal=(weight/height/height)*10000
                f = open('bmi.txt','a')
                f.write(f"name ={name} weight = {weight} height = {height} bmi_cal={bmi_cal} \n")
                f.close()
                a= bmi_cal
                if(a <= 18.5):
                    print("your weight is underweight")
                elif(18.5<a<25):
                    print("your weight is Normal ")
                elif(25<a<30):
                    print("your weight is Overweight and your BMI is  ")
                else :
                    print("Obesity")  
    except:
        print("please write proper information")
bmi()