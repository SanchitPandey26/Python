n = int(input())
arr = list(map(int, input().split()))
k = int(input())
arr[n-k:n] = arr[n-k:n][::-1]
arr[:n-k] = arr[:n-k][::-1]
arr[:] = arr[:][::-1]
for i in arr:
    print(i, end=' ')

'''
Approach --> Read Reversal algorithm approach in below article
Explanation --> https://takeuforward.org/data-structure/rotate-array-by-k-elements/
Video Explanation --> https://www.youtube.com/watch?v=wvcQg43_V8U&t=1218s
'''