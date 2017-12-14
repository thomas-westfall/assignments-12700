data = [21, 9, 5, 8, 10, 13]


def how_many_can_i_eat(data,value):
    ans = 0
    for x in data:
        if x < value:
            ans = ans + 1
    return ans
          

def canibals(data,target):
  ans = 0
  datab = data #avoid side effects
  
  for x in datab:
      if x > target: #already greater than target
          ans = ans + 1
          datab.remove(x)

  temp = 0 
  for x in datab:
      temp = x #avoid side effects
      
      if x <= target and (x + how_many_can_i_eat(datab, x) > target):
          for y in datab:
             if y < x and temp <= target:
                 temp = temp + 1

      if temp > target:
          ans = ans + 1
           

  return ans
          


print(canibals(data,10))
