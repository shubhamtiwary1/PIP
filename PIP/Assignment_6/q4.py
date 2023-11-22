def uppercase(a):
    ans = ""
    n=len(a)
    for i in range(0, n):
        if i==0 or a[i-1] == ' ':
            if 'a' <= a[i] <= 'z':
                c = chr(ord(a[i])-32)
                ans += c
        else:
            if 'A' <= a[i] <= 'Z':
                c = chr(ord(a[i])+32)
                ans += c
            else:
                ans += a[i]
    return ans
a=input()
print(uppercase(a))
