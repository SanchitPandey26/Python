# In python, we cannot use recursion for n > 998, as the maximum recursion memory is 1000.
# Maximum limit of n = 998 is because, 1 stack of memory is used for main and another function call in main.
# It gives an error "maximum recursion depth exceeded"

def print_nos(num):
    if num <= 0:
        return
    print(num, end=' ')
    print_nos(num - 1)


n = int(input())
print_nos(n)

'''
Make recursion tree to understand
'''