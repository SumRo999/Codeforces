numOfStone = int(input())
colorOfStone = list(input())
firstElement = colorOfStone[0]
count = 0
for i in colorOfStone:
    if i==firstElement:
        count=count+1
    else:
        firstElement = i
count = count-1
print(count)