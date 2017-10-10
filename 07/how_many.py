def freq(n,l):
    ans = 0
    for i in range(0,len(l)):
        if l[i] == n:
            ans = ans + 1
    return ans

def min(l):
    ans = l[0]
    for i in range(1,len(l)):
        if l[i] < ans:
            ans = l[i]
    return ans

def mode(l):
    ans = 0
    for i in range (0,len(l)):
        if freq(l[i],l) > ans:
            ans = l[i]
    return ans
