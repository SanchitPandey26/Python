def merge(lst, low, mid, high):
    temp = []
    left = low
    right = mid +1
    while left <= mid and right <= high:
        if lst[left] < lst[right]:
            temp.append(lst[left])
            left += 1
        else:
            temp.append(lst[right])
            right += 1

    while left <= mid:
        temp.append(lst[left])
        left += 1

    while right <= high:
        temp.append(lst[right])
        right += 1

    for i in range(low,high+1):
        lst[i] = temp[i-low]


def mergesort(lst, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergesort(lst, low, mid)
    mergesort(lst, mid + 1, high)
    merge(lst, low, mid, high)


n = int(input())
arr = list(map(int, input().split()))

mergesort(arr, 0, n - 1)

for i in arr:
    print(i, end=' ')

'''
Approach --> Read the below article
Explanation --> https://takeuforward.org/data-structure/merge-sort-algorithm/
Video Explanation --> https://youtu.be/ogjf7ORKfd8
'''
