def removespecials(word):
    result=""
    for l in word:
        if l.isalpha(): #is it not a special character
            result = result + l
    return result

def countoccs(wordlist):
    d={}
    l=[]
    listdone=[]
    for i in range(len(wordlist)-1):
        l=[]
        w = wordlist[i]
        if not w in listdone:
            for j in range(len(wordlist)-1):
                if wordlist[j] == w:
                    l.append(wordlist[j + 1])
            d.setdefault(w,0)
            d[w] = l
            listdone.append(w)
    return d

def counttextwords(f):
    f = open(f).read()
    l=[]
    for w in f.split():
        w = w.lower()
        w = removespecials(w)
        l.append(w)
    d = countoccs(l)
    return d


d = counttextwords("hamlet.txt")
print(d)
