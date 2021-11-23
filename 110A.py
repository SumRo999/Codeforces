line = input()
lucky_num = []

for i in line:
  if (i=='7' or i=='4'):
    lucky_num.append(i)
  else:
    continue

if (len(lucky_num) == 7 or len(lucky_num)== 4):
  print('YES')
else:
  print('NO')
