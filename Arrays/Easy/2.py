n = int(input())
arr = list(map(int, input().split()))
if n < 2:
    print(-1)
else:
    largest = arr[0]
    second_largest = float('-inf')      # Number smaller than any other number
    for i in arr:
        if i > largest and i > second_largest:
            second_largest = largest
            largest = i
        elif second_largest < i < largest:
            second_largest = i
    if second_largest == float('-inf'):
        print(-1)
    else:
        print(second_largest)

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/data-structure/find-second-smallest-and-second-largest-element-in-an-array/
Video Explanation --> https://www.youtube.com/watch?v=37E9ckMDdTk&t=810s
'''