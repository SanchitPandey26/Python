n = int(input())
arr = list(map(int, input().split()))
k = int(input())
dic = {}
maxLen = 0
subarray_sum = 0
for i in range(n):
    subarray_sum += arr[i]
    if subarray_sum == k:
        maxLen = max(maxLen, i + 1)
    rem = subarray_sum - k
    if rem in dic:
        subarray_len = i - dic[rem]
        maxLen = max(maxLen, subarray_len)
    if subarray_sum not in dic:
        dic[subarray_sum] = i
print(maxLen)

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/arrays/longest-subarray-with-sum-k-postives-and-negatives/
Video Explanation --> https://www.youtube.com/watch?v=frf7qxiN2qU
'''