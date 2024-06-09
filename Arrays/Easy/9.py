n = int(input())
arr = list(map(int, input().split()))
k = int(input())
flag = False
for i in arr:
    if i == k:
        flag = True
        break
print(flag)

'''
Approach --> Read in below article
Explanation --> https://takeuforward.org/data-structure/linear-search-in-c/
Video Explanation --> https://www.youtube.com/watch?v=wvcQg43_V8U&t=2465s
'''