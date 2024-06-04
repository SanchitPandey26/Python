n = int(input())
for i in range(n):
    for j in range(65, 66+i):   # "A" in ascii code is 65
        print(chr(j), end=' ')  # chr function returns the character for ascii code
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this pattern problem, instead of numbers, we have to print alphabets hence making the pattern look like a 
right-angled triangle. So, the outer loop will run for N rows and the inner loop will loop for i alphabets in each row
where i is the row number. Alphabets in each row will start from A each time we enter a new row and 
will loop till (A+i)th alphabet in that row.


Explanation --> https://takeuforward.org/pattern/pattern-14-increasing-letter-triangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=2922
'''
