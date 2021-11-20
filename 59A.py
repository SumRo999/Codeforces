line = input()
j = 0
k = 0
for i in line:
  if (i.isupper() == True):
    j = j+1
  else:
    k = k+1
if (k>=j):
  print(line.lower())
else:
  print(line.upper())