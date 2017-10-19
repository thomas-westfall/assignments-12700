#!/bin/python3
import sys
s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in raw_input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in raw_input().strip().split(' ')]



applec = 0
for x in apple:
    if (a + x <= t) and (a + x >= s):
        applec = applec + 1
print(applec)
    
orangec = 0
for x in orange:
    if (b + x <= t) and (b + x >= s):
        orangec = orangec + 1
print(orangec)