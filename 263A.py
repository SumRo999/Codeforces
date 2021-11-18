rows = 5
count = 0
chngrow = 0
chngcol = 0
while (count < rows):
    count = count+1
    row = list(map(int,input().split()))
    for i in row:
      colcount = colcount+1
      if (i==1):
        rowof1 = count
        colof1 = colcount
    if (i!=1):
        colcount = 0
#chngrow
if(rowof1==3):
  chngrow = chngrow
else:
  while(rowof1<4):
    rowof1 = rowof1+1
    chngrow = chngrow+1
    if(rowof1==3):
      break
  while(rowof1>3):
    rowof1 = rowof1-1
    chngrow = chngrow+1
    if(rowof1==3):
      break

#chngcol
if(colof1==3):
  chngrow = chngrow
else:
  while(colof1<3):
    colof1 = colof1+1
    chngcol = chngcol+1
    if(colof1==3):
      break
  while(colof1>3):
    colof1 = colof1-1
    chngcol = chngcol+1
    if(colof1==3):
      break
chng = chngrow+chngcol
print(chng)
