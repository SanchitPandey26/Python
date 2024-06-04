n = int(input())
for i in range(n):
    if i == 0 or i == n - 1:
        print('*' * n, end='')  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
    else:
        print('*' + ' ' * (n - 2) + '*', end='')  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

This problem is a very simple one where we just have to print a hollow rectangle. So, after observation, 
we see that the stars are only printed at the border of the rectangle, and on the rest of the positions, 
spaces are printed. Hence, the outer loop and inner loop both will loop for n times and in the inner loop we 
add a condition that if the row index or column index is equal to 0 or n-1, then stars should get printed otherwise
spaces should be printed.


Explanation --> https://takeuforward.org/pattern/pattern-21-hollow-rectangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=4349
'''
