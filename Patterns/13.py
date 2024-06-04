n = int(input())
num = 1
for i in range(n):
    for j in range(i+1):
        print(num, end=' ')
        num += 1
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we just have to print the right-angled number pyramid but here, 
we also have to increase the number each time we print it. 
For printing, the right-angled pyramid as we know the outer loop runs for N times and 
the inner loop runs for i times. Now, to print an increasing number pyramid we just have to increment the number
inside the inner loop so that after printing the number each time it increases by 1.




Explanation --> https://takeuforward.org/pattern/pattern-13-increasing-number-triangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=2812
'''
