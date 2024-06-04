n = int(input())
for i in range(n, 0, -1):
    for j in range(65, 65+i):   # "A" in ascii code is 65
        print(chr(j), end=' ')  # chr function returns the character for ascii code
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

This pattern problem is very similar to the last pattern problem we did where we had to print an 
increasing letter pyramid pattern but this time we have to print it in the reverse fashion. 
So, the outer loop will run for N rows and the inner loop will loop for i alphabets in each row 
(where i is the row number) because the 1st row will have alphabets from A to A+(N-1). 
Alphabets in each row will start from A each time we enter a new row and will loop till (A+i)th alphabet in that row.
In this way, the last row will only contain the alphabet A at last.


Explanation --> https://takeuforward.org/pattern/pattern-15-reverse-letter-triangle-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=3057
'''
