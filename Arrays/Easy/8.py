n = int(input())
arr = list(map(int, input().split()))
j = 0
for i in range(1, n):
    if arr[i] == 0 and arr[i - 1] != 0:
        j = i
    if arr[i] != 0 and arr[j] == 0:
        arr[j] = arr[i]
        arr[i] = 0
        j += 1
for i in arr:
    print(i, end=' ')

'''
Approach:
In this problem we will use two pointer approach. We will use j as a pointer for 0 elements in the array
and i as incrementing pointer for all elements of the array. We initialize j as 0, assuming the first
element is zero. Now we run a loop from second element to the last element of the array. We will
check if the ith element is zero and if it is we mark it with j pointer. In case there are repeating
zeros then the j pointer will mark only the last zero of the repeating ones, to counter this we will
add update our condition such that if the ith element is zero and its previous element is not zero,
then mark it with j pointer. Now, to move the zeroes at the end we check if the ith element is not and
the jth element is zero (we are checking the jth element to be zero because we assumed that the first
element is zero and marked j with, this condition will help us counter if the first element is not zero).
If the condition is true we swap the jth and ith element as we want the numbers to be first, put the
ith element as zero and increment j pointer by 1.
'''
