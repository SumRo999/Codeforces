str1 = input()
if (len(str1)<1 or len(str1)>100):
    str1 = input()
str2 = input()
if (len(str2) != len(str1)):
    str2 = input()
str1 = str1.lower()
str2 = str2.lower()
if (str1==str2):
    print('0')
elif (str1<str2):
    print('-1')
else:
    print('1')