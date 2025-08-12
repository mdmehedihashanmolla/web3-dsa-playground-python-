def Right_Angled_Triangle_Pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end=" ")
        print()

Right_Angled_Triangle_Pattern(5)