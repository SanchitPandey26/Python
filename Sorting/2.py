n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1,0,-1):
    didswap = 0
    for j in range(i):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    if didswap == 0:
        break

for i in arr:
    print(i, end=' ')

'''
Approach --> Read the below article
Explanation --> https://takeuforward.org/data-structure/bubble-sort-algorithm/
Video Explanation --> https://www.youtube.com/watch?v=HGk_ypEuS24&t=1061s
'''