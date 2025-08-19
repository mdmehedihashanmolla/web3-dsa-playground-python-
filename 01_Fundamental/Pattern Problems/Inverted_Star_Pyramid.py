def Inverted_Star_Pyramid(n):
    for i in range(n):
        for j in range(i):
            print("  ", end="")  
        for k in range(2 * (n - i) - 1):
            print("* ", end="")
        print() 

Inverted_Star_Pyramid(5)
