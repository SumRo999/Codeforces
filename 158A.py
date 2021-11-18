n=0
i=0
value = 0
numofperfinisher = list(map(int,input().split()))
numofpar = int(numofperfinisher[0])
finisher = int(numofperfinisher[1])-1
while (n==0):
    marks = list(map(int,input().split()))
    if(len(marks) != numofpar):
        print('Please enter', numofpar,'numbers')
    else:
        break
for i in marks:
    if i==0:
      continue
    elif i>=marks[finisher]:
        value = value + 1
    else:
        continue
print(value)