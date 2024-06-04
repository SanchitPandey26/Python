n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

This pattern is just a mixture of the last two patterns (erect pyramid and inverted pyramid).
Firstly, we will print the erect pyramid and then an inverted pyramid below it.


Explanation --> https://takeuforward.org/pattern/pattern-9-diamond-star-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=2056
'''
