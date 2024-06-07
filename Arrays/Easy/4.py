n = int(input())
arr = list(map(int, input().split()))
if n == 1:
    print(True)
else:
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i + 1]:
            count += 1
    if arr[0] < arr[n-1]:
        count += 1

    if count > 1:
        print(False)
    else:
        print(True)
'''
Approach:
Array rotation is a common computer programming operation that involves shifting the elements of an array 
by a specified number of positions. The given problem is to determine if an array can be considered a sorted array 
that has been rotated. A sorted array that is rotated would have at most one "drop" or point where an element 
is greater than the next element. If the array is rotated, the elements will eventually wrap around to the start 
of the array, i.e, the first element will always be greater than the last element in a sorted rotated array.
Therefore, we need to check if there is at most one such "drop" point.
'''