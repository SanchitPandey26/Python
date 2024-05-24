n = int(input())
c = 1;
for i in range(n):
    if (i % 2 == 0):
        print("1", end=" ")
        print("0 1 "*int((i/2)), end="")
    else:
        print("0 1 "*c, end="")
        c += 1
    print()