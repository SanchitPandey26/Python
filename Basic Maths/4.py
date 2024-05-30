n = int(input())
temp = n
rev = 0
if n < 0:
    print(False)
else:
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n //= 10
    if (rev == temp):
        print(True)
    else:
        print(False)