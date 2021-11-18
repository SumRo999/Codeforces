statements = int(input());
count = 0
X = 0
while (count < statements):
    count = count+1
    line = input()
    inc1 = "X++"
    inc2 = "++X"
    dec1 = "X--"
    dec2 = "--X"
    if (line==inc1 or line==inc2):
        X = X+1
    else:
        X = X-1
print(X)