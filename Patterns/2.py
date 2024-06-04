n = int(input())
for i in range(1,n+1):
    print("* "*i)   # String * n; prints the string n times. Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we run the outer loop for N times as we have to print N rows, and since we have to print a 
right-angled triangle/pyramid which must be upright, the inner loop will run for the row number in each iteration. 
For eg: 1 star for row 1, 5 stars for row 5, and so on.

Explanation --> https://takeuforward.org/pattern/pattern-2-right-angled-triangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=856
'''