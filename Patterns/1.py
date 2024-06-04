n = int(input())
for i in range(n):
    print("* " * n)  # String * n; prints the string n times. Hence, an inner loop is not required in python.

'''
Approach: 
There are 4 general rules for solving a pattern-based question: 

1. We always use nested loops for printing the patterns. 
   For the outer loop, we count the number of lines/rows and loop for them.
2. Next, for the inner loop, we focus on the number of columns and somehow connect them to the rows 
   by forming a logic such that for each row we get the required number of columns to be printed.
3. We print the ‘*’ inside the inner loop.
4. Observe symmetry in the pattern or check if a pattern is a combination of two or more similar patterns.

In this particular problem, we run the outer loop for N times since we have N rows to be printed,
the inner loop also runs for N times as we have to print N stars in each row. 
This way we get a rectangular star pattern (square) with an equal number of rows and columns.

Explanation --> https://takeuforward.org/pattern/pattern-1-rectangular-star-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=91
'''
