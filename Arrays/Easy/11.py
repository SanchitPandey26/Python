n = int(input())
arr = list(map(int, input().split()))
sum1 = n * (n+1)//2
sum2 = 0
for i in arr:
    sum2 += i
print(sum1-sum2)

'''
Approach --> Read optimal approach 1 in below article
Explanation --> https://takeuforward.org/arrays/find-the-missing-number-in-an-array/
Video Explanation --> https://www.youtube.com/watch?v=bYWLJb3vCWY&t=57s
'''