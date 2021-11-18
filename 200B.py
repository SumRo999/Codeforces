noOfBottle = int(input())
percentOfJuiceInBottles = list(map(int,input().split()))
sumOfpercentage = sum(percentOfJuiceInBottles)
volume = sumOfpercentage/noOfBottle
print(float(volume)) 