# In python, we cannot use recursion for n > 998,
# as it gives an error "maximum recursion depth exceeded"


def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


n = int(input())
print(factorial(n))