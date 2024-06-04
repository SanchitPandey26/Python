n = int(input())
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this particular pattern, we run the outer loop for N times as we have to print N rows as usual. 
Now, the question arises what will be the logic behind the inner loop?

Similar to the last pattern, we can clearly observe that for each row there are some spaces that get printed 
then some stars, and then again some spaces giving it an inverse pyramidal look. 
For eg: In the first row (i=0) there are 0 spaces, 9 stars, then again 0 spaces. 
In the second row (i=1) there is 1 space, 7 stars, then again 1 space so we can say that there are i spaces, 
2*N - (2*i+1) stars, and then again i space for each row where i is the row index. 
We thus simply run 3 inner loops, first for printing the spaces, then the stars, and then the spaces again.


Explanation --> https://takeuforward.org/pattern/pattern-8-inverted-star-pyramid/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=1870
'''