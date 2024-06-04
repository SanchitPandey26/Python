n = int(input())
count = 0
temp = n
while (temp > 0):
    digit = temp % 10
    if (digit != 0):
        if (n % digit == 0):
            count += 1
    temp //= 10

print(count)

'''
Approach:
In this problem, we need to take each digit of a number and check if the digit divides the number.
That is, number % digit = 0 should be true. So, we need to get the digits for the number. We know the approach for
retrieving the digits of a number: In a while loop with condition num > 0, digit = num % 10 & num //= 10. 
But this will update our original number. So, lets store the number in a temporary variable, and we get the digits
from the temporary variable, thus the number remains unaffected. After retrieving a digit we check if it divides the 
original number.
'''