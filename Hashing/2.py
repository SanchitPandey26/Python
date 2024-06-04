n = int(input())
lst = list(map(int, input().split()))
map = {}
for i in lst:
    if i in map:
        map[i] += 1
    else:
        map[i] = 1

max_key = next(iter(map))
min_key = next(iter(map))
for key in map:
    if map[key] > map[max_key]:
        max_key = key
    if map[key] < map[min_key]:
        min_key = key

print(max_key,min_key)

''' 
Approach --> Optimized approach(Using map) in the below article.
Explanation --> https://takeuforward.org/arrays/find-the-highest-lowest-frequency-element/
Video Explanation --> https://www.youtube.com/watch?v=KEs5UyBJ39g&t=2523s
'''