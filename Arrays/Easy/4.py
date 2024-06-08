n = int(input())
arr = list(map(int, input().split()))
j = 0
for i in range(n):
    if arr[j] != arr[i]:
        j += 1
        arr[j] = arr[i]

print(j+1)
for i in range(j+1):
    print(arr[i], end=' ')

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/data-structure/remove-duplicates-in-place-from-sorted-array/
Video Explanation --> https://www.youtube.com/watch?v=37E9ckMDdTk&t=1886s
'''