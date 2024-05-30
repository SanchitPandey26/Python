n = int(input())
rev = 0
if n > 0:
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
else:
    n //= -1
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    rev //= -1
print(rev)