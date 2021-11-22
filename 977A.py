line = list(map(int,input().split()))
n = line[0]
k = line[1]
while (k>0):
  last_digit = n%10
  if (last_digit == 0):
    n = n/10
    k = k-1
  else:
    n = n-last_digit
    k = k-last_digit
print(int(n))