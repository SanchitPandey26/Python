n = int(input())
arr = list(map(int, input().split()))
temp = arr[0]
for i in range(1, n):
    arr[i-1] = arr[i]
arr[n-1] = temp
for i in arr:
    print(i, end=' ')

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/data-structure/left-rotate-the-array-by-one/
Video Explanation --> https://www.youtube.com/watch?v=wvcQg43_V8U&t=61s
'''