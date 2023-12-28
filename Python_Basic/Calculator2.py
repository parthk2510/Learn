def Addition(x,y):
    return x+y 

def subtraction(x,y):
    return x-y 

def multiplication(x,y):
    return x*y

def Division(x,y):
    return x/y 

print("Select operation ")
print("1 addition \n 2.subtraction \n 3.Multiplication  \n 4.division ")

choice = int(input())
num1=int(input())
num2=int(input())


if choice == 1:
    print(Addition(num1 ,num2))
elif choice ==2:
    print(subtraction(num1,num2))
elif choice == 3:
    print(multiplication(num1,num2))
elif choice ==4 :
    print(Division(num1,num2))
else :
    print("invaild ") 
