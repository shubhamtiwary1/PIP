import math

# a:

a = int(input("Enter a: "))

b = int(input("Enter b: "))

c = int(input("Enter c: "))

xx = (b*b - (4*a*c))**0.5

root1 = ((-b) + xx)/(2 * a)

print(root1)

#b:

x = int(input("Enter x: "))
        
y = int(input("Enter y: "))

res = (((2*x*y) - (9*y)) / (2*x*y*y*y)) - ((4*y*x*x) / (2*y))

print(res)
