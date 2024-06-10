n = int(input())
arr = list(map(int, input().split()))
maxi = 0
count = 0
for i in arr:
    if i == 1:
        count += 1
        maxi = max(maxi,count)
    else:
        count = 0
print(maxi)

'''
Approach --> Read in below article
Explanation --> https://takeuforward.org/data-structure/count-maximum-consecutive-ones-in-the-array/
Video Explanation --> https://www.youtube.com/watch?v=bYWLJb3vCWY&t=1124s
'''