n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print(' ' * 2 * (n - i), end='')  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
    for j in range(i, 0, -1):
        print(j, end='')
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we want to print a combination of a numbered pyramid and a reverse-numbered pyramid. 
So, as per our observation in each row, numbers are printed from 1 to the row number and then some spaces 
and then again numbers from 1 to the row number but in reverse order. 
So, the outer loop will run from 1 to N and there will be three inner loops for numbers, spaces, and then again numbers.

The first inner loop will have numbers printed from 1 to the row number, 
the second will print the spaces ( 8 spaces in row 1, 6 spaces in row 2, and so on) and 
then the last loop will run from row number to 1 in decreasing manner. 
For spaces, we can say that initially, spaces are 2*(N-1) for Row 1 where N is the total no. of rows and 
then the spaces decrease by 2 in each iteration till the last row is reached. 


Explanation --> https://takeuforward.org/pattern/pattern-12-number-crown-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=2535
'''
