def comma(listc = []):
    ans = ""
    temp = 0
    for x in listc:
        temp += 1
        if temp != len(listc):
            ans = ans + x + ", "
        else:
            ans = ans + "and " + x
    return ans

spam = ['apples','bananas','tofu','cats']

print(comma(spam))