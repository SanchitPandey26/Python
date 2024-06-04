n = int(input())
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this particular pattern, we run the outer loop for N times as we have to print N rows as usual. 
Now, the question arises what will be the logic behind the inner loop?

As we can clearly observe that for each row there are some spaces that get printed then some stars 
and then again some spaces giving it a final pyramidal look. For eg: In the first row (i=0) there are 4 spaces,
1 star, then again 4 spaces. In the second row (i=1) there are 3 spaces, 3 stars, 
then again 3 spaces so we can say that there are N-i-1 spaces, 2*i+1 stars, 
and then again N-i-1 spaces for each row where i is the row index. 
We thus simply run 3 inner loops first for printing the spaces, then the stars, and then the spaces again.


Explanation --> https://takeuforward.org/pattern/pattern-7-star-pyramid/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=1473
'''
