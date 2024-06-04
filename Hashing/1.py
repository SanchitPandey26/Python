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

''' 
Approach --> Solution 2: Using Map in the below article.
Explanation --> https://takeuforward.org/data-structure/count-frequency-of-each-element-in-the-array/
Video Explanation --> https://www.youtube.com/watch?v=KEs5UyBJ39g&t=2319s
'''