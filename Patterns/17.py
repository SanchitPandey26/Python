n = int(input())
for i in range(n):
    print(' ' * (n - i - 1), end='')  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
    for j in range(i + 1):
        print(chr(65 + j), end='')
    for j in range(1, i + 1):
        print(chr(65 + i - j), end='')
    print(' ' * (n - i - 1), end='')  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we have to print an alphabet triangle as shown in the examples above where we can clearly observe that
the first row has only the letter A in the middle and some spaces on either side of it and the second row has 
the letters ABA and some spaces again on both sides. So, we observe from this that first there are some spaces, 
then letters increasing from A to A + i where i is the row number and then decreasing back to A, 
then finally some more spaces to the end. Hence, like all the previous patterns the outer loop will loop for N times 
and there will be four inner loops in this pattern.

The first inner loop is for printing the (N-i-1) spaces ( 1st row -> 4 spaces, 2nd row -> 3 spaces, and so on), 
the second and third one for printing the characters, and then the last one again for printing the spaces. 
For the first character loop, we print characters from A to A+i where i is the row number.
For the second character loop, we print characters from A+i-1 to A where i is the row number.


Explanation --> https://takeuforward.org/pattern/pattern-17-alpha-hill-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=3282
'''
