import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = pow(b, 2)-4*a*c

if D>0:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print("Two roots: " , x1, x2)
if D<0:
    print("No roots")
if D==0:
    x1=-b/(2*a)
    print("One root: ", x1)

