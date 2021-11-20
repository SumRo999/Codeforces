text = input()
s=set(text)
s="".join(s)
if (len(s)%2 == 0):
  print('CHAT WITH HER!')
else:
  print('IGNORE HIM!')

# set() --> A Set is an unordered collection
#           data type that is iterable, mutable,
#           and has no duplicate elements.
# "".join() --> It joins two adjacent elements in
#               iterable with any symbol defined in
#               "" ( double quotes ) and returns a
#               single string