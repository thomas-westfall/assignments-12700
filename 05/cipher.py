key = "abcdefghijklmnopqrstuvwxyz"
keyup = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_letter(c,r):
    if c in key:
        return (key[(key.index(c) + r) % 26])
    elif c in keyup:
        return (keyup[(keyup.index(c) + r) % 26])
    else:
        return c

print(encode_letter("y",3))


def encode_string(s,r):
    ans = ''
    for i in s:
            ans += encode_letter(i,r)
    return ans

print(encode_string("helLO?",3))


def full_encode(s):
    ans = ''
    for i in range (1,26):
        ans = ans + encode_string(s,i) + "\n"
    return ans

print(full_encode("yeS"))
    

def distance(l1,l2):
    length = len(l1)
    if length>len(l2):
        length = len(l2)

def build_frequency_vector(s):
    #count letters in string
    spaces = s.count(' ')
    num letters = len(s) = len(s) - spaces
    v= []
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)
    return v

def print_vector_table(v):
    s = "abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i] , " : " , v[i])
