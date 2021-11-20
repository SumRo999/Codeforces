distance = int(input())
steps = 1
if (distance>5):
  steps = int(distance/5)
  distance = distance - (5*steps)
  if (distance%5 == 4):
    steps = steps+1
    distance = distance-4
  elif (distance%5 == 3):
    steps = steps+1
    distance = distance-3
  elif (distance%5 == 2):
    steps = steps+1
    distance = distance-2
  elif (distance%5 == 1):
    steps = steps+1
    distance = distance-1
  elif (distance%5 == 0):
    distance = distance
else:
  steps=steps
print(steps) 