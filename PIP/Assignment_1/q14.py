a = int(input("Enter the number: "))
s = 0

rem = a%10
s += rem

a //= 10
rem = a%10
s += rem

a //= 10
rem = a%10
s += rem

a //= 10
rem = a%10
s += rem

print(s)
