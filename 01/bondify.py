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