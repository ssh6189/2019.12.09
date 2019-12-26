for i in range(2,10,4):
    for j in range(1, 10):
        for k in range(i, i + 4):
            print("%d x %d = %2d"%(k, j, k*j), end = "  ")
        print()
    print()

str(input())
