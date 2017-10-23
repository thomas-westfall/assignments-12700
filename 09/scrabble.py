def score(w):
    ans = 0
    ones = "aeioulnrst"
    twos = "dg"
    threes = "bcmp"
    fours = "fhvwy"
    fives = "k"
    eights = "jx"
    tens = "qz"

    for x in w:
        if x in ones:
            ans = ans + 1
        if x in twos:
            ans = ans + 2
        if x in threes:
            ans = ans + 3
        if x in fours:
            ans = ans + 4
        if x in fives:
            ans = ans + 5
        if x in eights:
            ans = ans + 8
        if x in tens:
            ans = ans + 10
            
    return ans

print(score("hello"))

