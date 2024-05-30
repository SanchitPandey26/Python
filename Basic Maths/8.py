import math

n = int(input())
flag = True
if (n == 0 or n == 1):
    flag = False
else:
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i == 0):
            flag = False
            break
print(flag)