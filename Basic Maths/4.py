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

'''
Approach --> Optimal approach in the below article
Explanation --> https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/
Video Explanation --> https://www.youtube.com/watch?v=1xNbjMdbjug&t=1230s
'''