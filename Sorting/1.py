n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1):
    mini = i
    for j in range(i,n):
        if arr[mini] > arr[j]:
            mini = j
    temp = arr[mini]
    arr[mini] =arr[i]
    arr[i] = temp

for i in arr:
    print(i, end=' ')

'''
Approach --> Read the below article
Explanation --> https://takeuforward.org/sorting/selection-sort-algorithm/
Video Explanation --> https://www.youtube.com/watch?v=HGk_ypEuS24&t=165s
'''