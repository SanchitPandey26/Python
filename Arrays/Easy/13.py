n = int(input())
arr = list(map(int, input().split()))
num = 0
for i in arr:
    num ^= i
print(num)

'''
Approach --> Read optimal approach in below article
Explanation --> https://takeuforward.org/arrays/find-the-number-that-appears-once-and-the-other-numbers-twice/
Video Explanation --> https://www.youtube.com/watch?v=bYWLJb3vCWY&t=1369s
'''