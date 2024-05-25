n = int(input())
for i in range(2*n-1):
    for j in range(2*n-1):
        top = i
        left = j
        bottom = 2*n-2-i
        right = 2*n-2-j
        print(n-min(min(top,bottom), min(left,right)), end='')
    print()