str1 = list(map(str,input().split('+')))
if (len(str1)<1 or len(str1)>100):
    str1 = list(map(str,input().split('+')))
str1 = sorted(str1)
print(*[i for i in str1], sep='+')