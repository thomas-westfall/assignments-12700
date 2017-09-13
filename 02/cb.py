def string_times(str, n):
  ans = ''
  for x in range(n):
    ans += str  
  return ans

def front_times(str, n):
  if len(str) > 3:
    ans = ''
    for x in range(n):
      ans += str[0:3]  
    return ans
  else:
    ans = ''
    for x in range(n):
      ans += str  
    return ans
    
def string_bits(str):
  ans = ''
  for x in range(len(str)):
    if x % 2 == 0:
      ans += str[x]
  return ans

def lone_sum(a, b, c):
  ans = 0
  if a != b and a != c:
     ans += a
  if b != a and b != c:
    ans += b
  if c != a and c != b:
    ans += c
  return ans

def string_splosion(str):
  ans = ''
  for x in range(len(str) + 1):
     ans += str[0:x]
  return ans

def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <= 60

def caught_speeding(speed, is_birthday):
  if is_birthday:
    if speed <= 65:
      return 0
    if speed >= 66 and speed <= 85:
      return 1
    else:
      return 2
        
  if speed <= 60:
    return 0
  if speed >= 61 and speed <= 80:
    return 1
  else:
    return 2
  

print (string_times('hi',3))
print (front_times('Chocolate', 2))
print (string_bits('Heeololeo'))
print (lone_sum(3, 2, 3))
print (string_splosion('Code'))
print (cigar_party(30, False))
print (caught_speeding(85, True))
