weight = int(input());
if(weight<=100 and weight>=1):
  if (weight == 2):
      print('NO')
  elif(weight % 2 == 0):
      print('YES')
  else:
      print('NO')
else: 
  print("Please enter a number between 1 to 100")