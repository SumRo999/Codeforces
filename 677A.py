first_line = list(map(int,input().split()))
second_line = list(map(int,input().split()))
n = 0
for i in second_line:
  if i>first_line[1]:
    n = n+2
  else:
    n = n+1
print(n)