n = int(input())
lst = list(map(int, input().split()))
map = {}
for i in lst:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1

for key,value in map.items():
    print(key, value)