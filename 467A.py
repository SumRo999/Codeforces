first_line = int(input())
i = 0
while first_line>0:
  pq = list(map(int,input().split()))
  first_line = first_line - 1

  p = pq[0]
  q = pq[1]
  space = q-p
  if (space>=2):
    i = i+1
  else:
    continue

print(i)