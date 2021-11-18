line = list(map(int,input().split()))
M = line[0]
N = line[1]
mul = M*N
if (mul%2==0):
    div = mul/2
else:
    div = mul/2
print(int(div))