def encode(s): # unsure if str.count() is allowed, O(N^2)
    ans=[]
    tempfreq=0
    i=0
       
    while i < len(s) - 1:
        j = i
        tempfreq = 0
        while (s[j:j+1] == s[i:i+1]):
            tempfreq=tempfreq + 1
            j = j + 1
        if tempfreq != 1:
            ans.append(tempfreq)
        ans.append(s[i:i+1])
        i = i + tempfreq
        
    return ans


print(encode("aaaaa"))
print(encode("bbaaa"))
print(encode("aabcccdeeeeaaa"))
            
