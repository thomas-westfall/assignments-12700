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
    for i in range(len(wordlist)-2):
        l=[]
        ltemp=[]
        w = wordlist[i]
        w2 = wordlist[i+1]
        if not w in listdone and not w2 in listdone:
            for j in range(len(wordlist)-1):
                if wordlist[j] == w and wordlist[j+1] == w2:
                    l.append(wordlist[j + 2])
            d.setdefault(w,0)
            d["(\""+ w + "," + w2+ "\")"] = l
            listdone.append(w)
            listdone.append(w2)
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
#d = counttextwords("test.txt")
print(d)
