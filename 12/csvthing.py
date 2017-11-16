import csv


def reader():
    mydict = {}
    with open('offenders-clean.csv') as csvfile:
        readstuff = csv.reader(csvfile)
        for row in readstuff:
            row[1] = row[1].split()
            for word in row[1]:
                mydict[word] = []
            for k, v in mydict.iteritems():
                for word in row[1]:
                    if k == word:
                        v = v.append(row[8])
    return mydict


#print(reader())

def countpeople(d, word):
    ans = []
    for key, value in d.items():
        if word in value[0]:
            ans.append(key)
    return ans


print(countpeople(reader(),"sorry"))
