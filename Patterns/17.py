n = int(input())
for i in range(n):
    print(' '*(n-i-1), end='')
    for j in range(i+1):
        print(chr(65+j), end='')
    for j in range(1, i+1):
        print(chr(65+i-j), end='')
    print()