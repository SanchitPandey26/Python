n = int(input())
for i in range(n + 1):
    print("*" * i)  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
for i in range(n - 1, 0, -1):
    print("*" * i)  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we have to print only the right half of the star diamond pattern 
as discussed in the previous article.So, as we can observe from the examples for N = 3 we have 5 rows, 
and for N = 6 we have 11 rows, hence the outer loop will run for 2*N -1 times. 
For the inner loop where we print the stars if row no. is less than or equal to N, 
then we observe that the stars which are printed in each row are equal to the row index itself. 
But, when i becomes more than N, then the no. of stars decreases by 1 with each increasing row. 
So, therefore the stars printed would be 2*N - i after i becomes greater than N.


Explanation --> https://takeuforward.org/pattern/pattern-10-half-diamond-star-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=2112
'''

