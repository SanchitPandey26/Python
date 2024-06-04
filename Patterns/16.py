n = int(input())
for i in range(n):
    ch = 65 + i             # "A" in ascii code is 65
    print(chr(ch)*(i+1))    # chr function returns the character for ascii code. i + 1 as i = 0 for first iteration
    # String * n; prints the string n times. Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this pattern problem, as we can observe we have to print a right-angled pyramid just like our last pattern 
but with a twist. Here, in every row, we have to print the same character i times where i is the row number. 
For example, the 1st row will print 1 A, the 2nd row will print 2 B’s, and so on. 
So, similar to the previous patterns the outer loop will loop for N times and the inner loop for i times 
with the character value incrementing each time we enter a new row.


Explanation --> https://takeuforward.org/pattern/pattern-16-alpha-ramp-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=3183
'''
