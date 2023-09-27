import math

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

max = max(a, max(b,c))
min = min(a, min(b,c))

print(max, min)

x = a+b+c
print(x-max-min)
