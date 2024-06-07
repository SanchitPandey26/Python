n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(True)
else:
    flag = True
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            flag = False
            break
    print(flag)

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/data-structure/check-if-an-array-is-sorted/
Video Explanation --> https://www.youtube.com/watch?v=37E9ckMDdTk&t=1722s
'''