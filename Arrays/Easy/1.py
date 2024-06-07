n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(arr[0])
else:
    largest = arr[0]
    for i in arr:
        if largest < i:
            largest = i
    print(largest)

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/data-structure/find-the-largest-element-in-an-array/
Video Explanation --> https://www.youtube.com/watch?v=37E9ckMDdTk&t=530s
'''