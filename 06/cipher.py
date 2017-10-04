import math
real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]

def rotate_char(c,r):
    """
    Rotates character c by amount r. Wraps if past z
    """
    v = ord(c)
    v = v - 97 # shift down so that 'a' is 0
    v = (v + r)%26
    v = v + 97 # shift back up so that 'a' is 97
    result = chr(v)
    return result

def encode_string(s,r):
    """
    rotate a string (lower case letters only)
    """
    result = ""
    for letter in s:
        if letter in "abcdefghijklmnopqrstuvwxyz":
            letter = rotate_char(letter,r)
        result = result + letter
    return result

def distance(l1,l2):
    """
    Euclidean distance between l1 and l2. If the lists are of 
    different lengths, go to the lenght of the shorter one
    """
    length = len(l1)
    if length>len(l2):
        length = len(l2)
    sum=0
    for i in range(length):
        sum = sum + (l1[i]-l2[i])*(l1[i]-l2[i])
    d = math.sqrt(sum)
    return d
    
def build_frequency_vector(s):
    # count the letters in the string
    spaces = s.count(' ')
    num_letters = len(s) - spaces
    v=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        v.append(s.count(letter) / num_letters)

    return v

def print_vector_table(v):
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(26):
        print(s[i]," : ",v[i])


def decode(s):
    lq=[]
    x=0
    dsmall= distance(build_frequency_vector(s),real_stats)
    sbest=''
    
    for i in range(1,26):
        lq.append(build_frequency_vector(encode_string(s,i)))
    for i in lq:
        x = x + 1
        if distance(i,real_stats) < dsmall:
            dsmall = distance(i,real_stats)
            sbest = encode_string(s,x)
    return sbest


s = "this is a longer sentence with more letters so hopefully it will be closer to the real distribution"

r = encode_string(s,2)

print(r)
print(decode(r))


f = build_frequency_vector(s)

print(distance(real_stats,f))
print("\n--------------------------------------\n")
f = build_frequency_vector(r)
print(distance(real_stats,f))
