# In python, we cannot use recursion for n > 998, as the maximum recursion memory is 1000.
# Maximum limit of n = 998 is because, 1 stack of memory is used for main and another function call in main.
# It gives an error "maximum recursion depth exceeded"

def sum_of_series(num):
    if num <= 0:
        return 0
    return num**3 + sum_of_series(num - 1)


n = int(input())
print(sum_of_series(n))

'''
Make recursion tree to understand
'''