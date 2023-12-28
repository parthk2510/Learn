print("Calculator")

print("Enter the opration you want to do \n 1. Addition \n 2.suntraction \n 3.multiplication \n 4.Division ")
choice = int(input())
print("Enter you number ")
a = int(input())
b = int(input())


if choice == 1:
    sum = a+b
    print(sum)
elif choice == 2:
    sub = a-b
    print(sub)
elif choice == 3:
    multi = a*b
    print(multi)
else:
    div = a/b
    print(div)
