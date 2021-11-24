k,l,m,n,d = int(input()),int(input()),int(input()),int(input()),int(input())
count = 0
for i in range(1,d+1):
  if (i%k == 0):
    count += 1
  elif (i%l == 0):
    count += 1
  elif (i%m == 0):
    count += 1
  elif (i%n == 0):
    count += 1
  else:
    continue
print(count)