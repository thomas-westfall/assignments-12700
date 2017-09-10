x = "word1 word2"
xc = ''

i = 1
xc += x[0].capitalize()

while (x[i] != ' '):
    xc += x[i]
    i += 1
    

i += 1
xc = xc + " " + x[i].capitalize()
i += 1


while (i <= len(x) - 1):
    xc += x[i]
    i += 1
    
print(xc)