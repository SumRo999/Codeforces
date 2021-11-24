n = int(input())
i = 1
a = list()
while n >= i:
    a.append('I')
    if i % 2 == 0:
        a.append('love')
    else:
        a.append('hate')
    if i == n:
        break
    else:
        a.append('that')
    i += 1

a.append('it')
print(' '.join(a))