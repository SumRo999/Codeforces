line = list(map(int,input().split()))
n = line[0]
k = line[1]
i = 0
while (k>i):
  last_digit = n%10
  if (last_digit == 0):
    n = n/10
    i = i+1
  else:
    n = n-1
    i = i+1

print(int(n))