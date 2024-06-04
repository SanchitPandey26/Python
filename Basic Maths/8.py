import math

n = int(input())
flag = True
if n == 0 or n == 1:
    flag = False
else:
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            flag = False
            break
print(flag)

'''
Approach --> Optimal approach in the below article
Explanation --> https://takeuforward.org/data-structure/check-if-a-number-is-prime-or-not/
Video Explanation --> https://www.youtube.com/watch?v=1xNbjMdbjug&t=2381s
'''