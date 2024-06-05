n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    j = i
    while j > 0 and arr[j-1] > arr[j]:
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        j -= 1

for i in arr:
    print(i, end=' ')

'''
Approach --> Read the below article
Explanation --> https://takeuforward.org/data-structure/insertion-sort-algorithm/
Video Explanation --> https://www.youtube.com/watch?v=HGk_ypEuS24&t=1900s
'''