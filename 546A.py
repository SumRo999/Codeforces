count = 0
totalPrice = 0
line = list(map(int,input().split()))
priceOfFirstBanana = line[0]
totalDollars = line[1]
numOfBananas = line[2]

while(count<numOfBananas):
  count = count+1
  priceOfBanana = count*priceOfFirstBanana
  totalPrice = totalPrice + priceOfBanana

if (totalPrice>totalDollars):
  amountToBorrow = totalPrice-totalDollars
  print(amountToBorrow)
else:
  print('0')