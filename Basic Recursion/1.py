# In python, we cannot use recursion for n > 998, as the maximum recursion memory is 1000.
# Maximum limit of n = 998 is because, 1 stack of memory is used for main and another function call in main.
# It gives an error "maximum recursion depth exceeded"

def print_string(num):
    if num <= 0:
        return
    print("Hey", end=' ')
    print_string(num - 1)


n = int(input())
print_string(n)

'''
We will try to understand by making a recursion tree:
Lets take n = 5. So in the above code 5 is passed into the function when the function is called in main.
In the function it checks the if condition, which is not true for n = 5, therefore it moves to next line.
The program prints "Hey" and once again the function is called but with n = 4.
The above steps repeat till n = 0, and when n = 0 then the all the functions in my stack memory ends.  
'''