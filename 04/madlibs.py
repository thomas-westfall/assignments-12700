import random
story = 'There lives a NOUN called NAME who VERB magical NOUN under a bridge. NAME loved to VERB that bridge in the summertime \
blah NAME blah NOUN ADJECTIVE VERB VERB blah'

nouns = ['girl','boy', 'cat']
verbs = ['eat','throw','run', 'walk', 'sleep', 'play']
adjectives = ['slow','quick','quiet']
names = ['Bob', 'Joe', 'Carl']

ans = ""
r = random.randint(0,len(nouns) - 1)
rv = random.randint(0,len(verbs) - 1)
ra = random.randint(0,len(adjectives) - 1)
rn = random.randint(0,len(names) - 1)

story.split()
s2 = story.split()
for x in range (len(s2)):
    if s2[x] == 'NAME':
        s2[x] = names[rn]
    if s2[x] == 'NOUN':
        s2[x] = nouns[r]
        r = random.randint(0,len(nouns) - 1)
    if s2[x] == 'VERB':
        s2[x] = verbs[rv]
        rv = random.randint(0,len(verbs) - 1)
    if s2[x] == 'ADJECTIVE':
        s2[x] = adjectives[ra]
        ra = random.randint(0,len(verbs) - 1)
    
    if x != len(s2) - 1:
        ans = ans + s2[x] + " "
    else:
        ans = ans + s2[x] + "."
    
print(ans)
