n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i, end="")
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this pattern, we run the outer loop for N times as we have to print N rows, 
and since we have to print a right-angled triangle/pyramid which must be upright, 
so the inner loop will run for the row number in each iteration. 
For eg: 1’s for row 1, 5’s 5 times for row 5, and so on. 
The only difference between this pattern and pattern 2 is that 
here we print numbers in each row instead of printing stars.


Explanation --> https://takeuforward.org/pattern/pattern-4-right-angled-number-pyramid-ii/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=1198
'''