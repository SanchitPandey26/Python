# In python, we cannot use recursion for n > 998,
# as it gives an error "maximum recursion depth exceeded"

def print_nos(num):
    if num <= 0:
        return
    print_nos(num - 1)
    print(num, end=' ')


n = int(input())
print_nos(n)
