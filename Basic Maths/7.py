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