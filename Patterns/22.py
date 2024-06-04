n = int(input())
for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        bottom = 2*n-2-i
        right = 2*n-2-j
        print(n-min(min(top,bottom), min(left,right)), end='')
    print()

'''
Approach: 
Read article to understand.

Explanation --> https://takeuforward.org/pattern/pattern-22-the-number-pattern/
Video Explanation--> https://youtu.be/tNm_NNSB3_w?t=4541
'''
