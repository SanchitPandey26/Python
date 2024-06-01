# In python, we cannot use recursion for n > 998,
# as it gives an error "maximum recursion depth exceeded"

def print_string(num):
    if num <= 0:
        return
    print("Hey", end=' ')
    print_string(num - 1)


n = int(input())
print_string(n)


