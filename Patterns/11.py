n = int(input())
count = 1
for i in range(n):
    if (i % 2 == 0):
        print("1", end=" ")
        print("0 1 " * int((i / 2)), end="")  # String * n; prints the string n times.
    # Hence, an inner loop is not required in python.
    else:
        print("0 1 " * count, end="")  # String * n; prints the string n times.
        # Hence, an inner loop is not required in python.
        count += 1
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this problem, we have to print binary digits alternatively in each row and column as shown in the examples. 
Let’s say that the first row starts with the binary digit ‘1’, the second row must start with ‘0’ 
and then the 3rd row with ‘1’ again, and so on. Similar is the case for the columns as well. 
For even no. of rows, the start is 1 and is followed by a combination of 0 and 1 repeated row-index/2 times.
For odd no. of rows, the combination of 0 and 1 is repeated certain number of times, lets call it count.
We can see that the count increases by one for every odd row. 
Lets, initialize the count variable with 1, for odd number of rows.
Now we run a loop for N times since we have N rows to be printed; for every even row, we print 1 once and 
print a combination of 0 and 1 i/2 times (i is the row index). For every odd row, we print a combination of 0 and 1
count number of times and increment the count by 1 for the next odd row.


Explanation --> https://takeuforward.org/pattern/pattern-11-binary-number-triangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=2362
'''
