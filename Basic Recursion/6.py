# In python, we cannot use recursion for n > 998,
# as it gives an error "maximum recursion depth exceeded"

def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


n = int(input())
print(fibonacci(n))
