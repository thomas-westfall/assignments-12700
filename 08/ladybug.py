#!/bin/python3
import sys


def check(n,b):
    for x in b: 
        
        if b.count(x) == 1 and x != "_":
            return "NO"
    
    for i in range(1,n-1):
        if (b.count("_") == 0) and ((b[i] != b[i-1]) and (b[i] != b[i+1])):
            return "NO"
        
    return "YES"
        


Q = int(raw_input().strip())
print("\n")
for a0 in range(Q):
    n = int(raw_input().strip())
    b = raw_input().strip()
    print(check(n,b))
                
        
