n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-1-j), end='')
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we have to print an alpha triangle as shown in the examples above. 
We observe from the examples that each row ends with the letter E in the case when N = 5 ( ‘A’ + 4 ). 
Also the triangle has to be right-angled so like the previous patterns, the outer loop will run for N times and 
the inner loop for i times. In the inner loop, we’ll start from the letter that comes i before 
the (‘A’ + N -1)th letter and then run the loop till we reach (‘A’ + N-1) in every row. 
For example, for N = 5 in each row, the letters will be printed from ‘E’ - i to ‘E’ where i is the row index.


Explanation --> https://takeuforward.org/pattern/pattern-18-alpha-triangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=3585
'''
