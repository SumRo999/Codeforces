y = int(input())
while (y<=9000 or y>=1000):
  y = y+1
  str_y = str(y)
  if (str_y[0] != str_y[1] and str_y[0] != str_y[2] and str_y[0] != str_y[3]) and (str_y[1] != str_y[2] and str_y[1] != str_y[3]) and (str_y[2] != str_y[3]) :
    break

print(y)

