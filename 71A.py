lines = int(input())
count = 0
while (count < lines):
    count = count+1
    word = input()
    if (len(word)>10):
        print(word[0], end='')
        print(len(word) - 2, end='')
        print(word[-1])
    else:
        print(word)