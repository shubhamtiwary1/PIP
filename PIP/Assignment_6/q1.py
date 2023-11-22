def update(s):
    n = len(s)
    i = 1
    ans = s[0]
    while(i<n):
        if(s[i] == s[i-1]):
            ans = ans+'*'
        else:
            ans = ans+s[i]
        i=i+1
    return ans
s = input()
print(update(s))
