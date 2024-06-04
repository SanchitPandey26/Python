n = int(input())
for i in range(n, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

Contrary to the previous patterns, this pattern observes symmetry. We can clearly see that the 
first half of the pattern is just a mirror image of the second half of the pattern. 
If we observe the first part, we see that like some previous patterns, it can also be divided into 3 parts i.e. stars,
 spaces, and then stars. In the first row, there are no spaces and 10 stars, in the second row, 
 there are 2 spaces and 8 stars, and so on. So, we initialize the spaces with 0 initially which will 
 eventually increment by 2 whenever we enter a new row. The stars, however, will be twice the row number, 
 half of the stars would be printed before the spaces and half after the spaces.


Explanation --> https://takeuforward.org/pattern/pattern-19-symmetric-void-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=3688
'''
