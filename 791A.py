count = 0
weights = list(map(int,input().split()))
limak = weights[0]
bob = weights[1]

while(limak<=bob):
  count = count+1
  limak = 3*limak
  bob = 2*bob

print(count)