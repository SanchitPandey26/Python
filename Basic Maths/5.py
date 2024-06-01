n = int(input())
temp = n
sum = 0
# count = int(math.log10(n) + 1)
while n > 0:
    digit = n % 10
    sum += digit**3    #Only for 3 digit number
    ''' If the number is not three digit -->
        sum += digit**count
    '''
    n //= 10
if (sum == temp):
    print("Yes")
else:
    print("No")
