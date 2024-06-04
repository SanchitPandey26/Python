n = int(input())
for i in range(n,0,-1):
    print("* "*i)   # String * n; prints the string n times. Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this pattern, we run the outer loop for N times as we have to print N rows and 
since we have to print a right-angled triangle/pyramid which must be inverted, 
the inner loop will run in decreasing order of stars, 
for eg: Row 1 (i=0) would contain N stars, Row 2 (i=1) would contain (N -1) stars and so on.


Explanation --> https://takeuforward.org/pattern/pattern-5-inverted-right-pyramid/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=1261
'''