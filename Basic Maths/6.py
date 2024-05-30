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