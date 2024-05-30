n1 = int(input())
n2 = int(input())
a = n1, b = n2 # We are assigning n1 and n2 to a and b because it is not good practice to change input value
while(a>0 and b>0):
    if a>b:
        a %= b  # we are changing the values of a here
    else:
        b %= a # we are changing the values of b here
if a == 0:
    print(b)
if b == 0:
    print(a)