for i in range(5):
    for j in range(5):
        if i == 5//2 or j == 5//2:
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()
                