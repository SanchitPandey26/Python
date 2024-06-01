# In python, we cannot use recursion for n > 998,
# as it gives an error "maximum recursion depth exceeded"

def sum_of_series(num):
    if num <= 0:
        return 0
    return num**3 + sum_of_series(num - 1)


n = int(input())
print(sum_of_series(n))