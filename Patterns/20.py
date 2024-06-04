n = int(input())
for i in range(1, n + 1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
for i in range(n - 1, 0, -1):
    print('*' * i + ' ' * (2 * (n - i)) + '*' * i)  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we have to print a butterfly-like star pattern. This pattern is very similar to Pattern 10 
in this series as here we can see that for Row 1 we have 2 stars, and 8 spaces, and for Row 2 we have 4 stars and 
6 spaces, and so on. Also, after the nth row, the stars decrease and the spaces increase. 
So, the outer loop will run for 2*n -1 times ( n times when spaces > stars and then n-1 when stars > spaces ). 
There will be 3 inner loops, one to print stars, then spaces, and then again stars. Spaces will decrement by 2 
as i increases and when i reaches n, then spaces decrement by 2 every time we enter a new row. 
When i<n, the stars printed in each row are 2*i, and as soon as i>n, the stars in each row would be twice of 2*n-i.


Explanation --> https://takeuforward.org/pattern/pattern-20-symmetric-butterfly-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=3996
'''
