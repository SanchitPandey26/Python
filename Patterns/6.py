n = int(input())
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()

'''
Approach: 
The are 4 general rules for solving a pattern-based question is same as previous one.

In this pattern, we run the outer loop for N times as we have to print N rows and 
since we have to print a right-angled triangle/pyramid which must be inverted, 
so the inner loop will run from 1 to (N-i)th integer in every row till we reach the Nth row 
where only ‘1’ would be left to get printed. For eg: in the 1st-row numbers from 1 to N get printed, 
in the 2nd-row numbers from 1 to (N-1) get printed, and so on.


Explanation --> https://takeuforward.org/pattern/pattern-6-inverted-numbered-right-pyramid/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=1419
'''