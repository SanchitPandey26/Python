n = int(input())
sum = 0
''' Good Approach --> Runtime is very high for long numbers
for i in range(1, n+1):
    for j in range(1, int(math.sqrt(i)+1)):
        if i % j == 0:
            sum += j
            if i//j != j:
                sum += i//j
print(sum)
'''

# Optimal Approach -->
for i in range(1, n+1):
    sum += n//i * i
print(sum)

'''
Arithmetic explanation for optimal approach:
Suppose we are given N = 5, now we have to find factors of 1, 2, 3, 4, 5 that will be
f1=1, f2=1+2, f3=1+3, f4=1+2+4, f5=1+5, and then we try to sum them so ans will be 
ans  =  f1 + f2 + f3 + f4 + f5 = 1 + (1 + 2) + (1 + 3) + (1 + 2 + 4) + (1 + 5)  (equals  21) 
now club alike terms
ans = (1x5) + (2x2) + (3x1) + (4x1) + (5x1) (remains 21)
now this part does the main trick and here I will do some rewriting as 
ans = (1 x (5/1) ) + (2 x(5/2)) + (3x(5/3)) + (4 x (5/4)) + (5x(5/5))  (still remains 21)
here I am doing floor division so example 3/2 = 1 and 7/3 =2
You can See answer remains same so here is our pattern that for any N 
ans = (1 x (N/1)) + (2 x (N/2)) + (3x(N/3)) + ... + (Nx(N/N)) 
'''