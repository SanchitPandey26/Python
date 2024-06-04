import math

n = int(input())
divisors = []
for i in range(1, int(math.sqrt(n)+1)):
    if n % i == 0:
        divisors.append(i)
        if n//i != i:
            divisors.append(n//i)
divisors.sort()
for i in divisors:
    print(i, end=' ')

'''
Approach --> Optimal approach in the below article
Explanation --> https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/
Video Explanation --> https://www.youtube.com/watch?v=1xNbjMdbjug&t=1580s
'''