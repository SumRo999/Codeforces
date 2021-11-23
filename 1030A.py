n = int(input())
line = list(map(int,input().split()))
easy = list()

for i in line:
  if i==1:
    print('HARD')
    break
  else:
    easy.append(i)
if len(easy) == n:
  print('EASY')