def partition(lst, low, high):
    pivot = lst[low]
    i = low
    j = high
    while i < j:
        while lst[i] <= pivot and i < high:
            i += 1
        while lst[j] > pivot and j > low:
            j -= 1
        if i < j:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
    temp = lst[low]
    lst[low] = lst[j]
    lst[j] = temp
    return j


def quicksort(lst, low, high):
    if low < high:
        pindex = partition(lst,low,high)
        quicksort(lst, low, pindex-1)
        quicksort(lst, pindex + 1, high)


n = int(input())
arr = list(map(int, input().split()))

quicksort(arr, 0, n - 1)

for i in arr:
    print(i, end=' ')

'''
Approach --> Read the below article
Explanation --> https://takeuforward.org/data-structure/quick-sort-algorithm/
Video Explanation --> https://youtu.be/WIrA4YexLRQ
'''
