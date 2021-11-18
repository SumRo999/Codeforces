lines = int(input());
count = 0
soln = 0
while (count < lines):
    count = count+1
    line = input()
    a = int(line[0])
    b = int(line[2])
    c = int(line[4])
    if (a==1 and b==1 or b==1 and c==1 or a==1 and c==1 or a==1 and b==1 and c==1):
        soln = soln+1
    else:
        soln = soln
print(soln)