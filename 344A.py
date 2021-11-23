first_line = int(input())
magnet = list()

while first_line>0:
  lines = input()
  first_line = first_line - 1
  magnet.append(lines)

i = 1
j = 1
while i<len(magnet):
  if magnet[i-1] == magnet[i]:
    i = i+1
  else:
    i = i+1
    j = j+1

print(j)