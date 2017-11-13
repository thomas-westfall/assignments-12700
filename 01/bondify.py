name = 'Firstname Lastname'
first = ''
last = ''

i = 0

while (name[i] != ' '):
    first += name[i]
    i += 1

i += 1

while (i <= len(name) - 1):
    last += name[i]
    i += 1

bondify = last + ', ' + first + ' ' + last

print(bondify)

#name ="James Bond"
#sloc = name.find(" ")
#first = name[0:sloc]
#last = name[sloc+1:]
#intro_string = last = ", " + name
#print(intro_string)