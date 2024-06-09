n = int(input())
a = list(map(int, input().split()))
k = int(input())
b = list(map(int, input().split()))
lst = []
i = 0
j = 0
while i < n and j < k:
    if a[i] <= b[j]:
        if len(lst) == 0 or lst[len(lst)-1] != a[i]:
            lst.append(a[i])
        i += 1
    else:
        if len(lst) == 0 or lst[len(lst)-1] != b[j]:
            lst.append(b[j])
        j += 1
while i < n:
    if len(lst) == 0 or lst[len(lst) - 1] != a[i]:
        lst.append(a[i])
    i += 1
while j < k:
    if len(lst) == 0 or lst[len(lst) - 1] != b[j]:
        lst.append(b[j])
    j += 1

for i in lst:
    print(i, end=' ')

'''
Approach --> Read in below article
Explanation --> https://takeuforward.org/data-structure/linear-search-in-c/
Video Explanation --> https://www.youtube.com/watch?v=wvcQg43_V8U&t=2465s
'''