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

'''
Approach --> Optimal approach in the below article
Explanation --> https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/
Video Explanation --> https://www.youtube.com/watch?v=1xNbjMdbjug&t=1418s
'''