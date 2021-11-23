total_stops = int(input())
n = 0
passengers = 0
k = list()
while (n<total_stops):
  stops = list(map(int,input().split()))
  exit = stops[0]
  enter = stops[1]
  passengers = passengers - exit + enter
  k.append(passengers)
  n = n+1
print(max(k))
