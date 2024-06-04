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

'''
Approach --> Optimal approach in the below article
Explanation --> https://takeuforward.org/maths/reverse-digits-of-a-number
Video Explanation --> https://www.youtube.com/watch?v=1xNbjMdbjug&t=930s
'''