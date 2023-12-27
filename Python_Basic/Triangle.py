print("Enter all the side of triangle ")
a = int(input())
b = int(input())
c = int(input())

a1 = a*a
b1 = b*b
c1 = c*c
sum = b1+c1

if a == b == c:
    print("It is a equilaterial triangle ")
elif a != b !=c:
    print("It is a scalene triangle")
elif a1 > sum & a1 < sum:
    print("It is not a right angle triangle ")
elif b == c:
    print("It is  a isoceles triangle ")
elif a == c:
    print("It is a isoceles triangle")
elif a == b:
    print("It is a isoceles triangle")
else:
    print("It is a right angle triangle ")
