for i in range(1,6):
    for b in range(1,6-i):
        print(" ",end="")
    for j in range(i,1-1,-1):
        print(j,end="")
    print()