def Inverted_Right_Pyramid(n):
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(" * ", end=" ")
        print()

Inverted_Right_Pyramid(5)