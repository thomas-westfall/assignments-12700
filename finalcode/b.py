data = [
  [1,1,2],
  [2,2,0.5],
  [-1,-3,2],
  [5,2,1]
  ]

def bounding_rect(data):
  ans = []
  temp = []
  minx = 0
  miny = 0
  maxx = 0
  maxy = 0

  for x in data:
      if x[0] + x[2] > maxx:
          maxx = x[0] + x[2]
      if x[0] - x[2] < minx:
          minx = x[0] - x[2]
      if x[1] + x[2] > maxy:
          maxy = x[1] + x[2]
      if x[1] - x[2] < miny:
          miny = x[1] - x[2]

  temp.append(minx)
  temp.append(miny)
  ans.append(temp)
  temp = []
  temp.append(maxx)
  temp.append(maxy)
  ans.append(temp)
  temp = []
  temp.append(maxx)
  temp.append(miny)
  ans.append(temp)
  temp = []
  temp.append(minx)
  temp.append(maxy)
  ans.append(temp)
  return ans


print (bounding_rect(data))
