def matrix_B(cube):
    for i in range(3):
        for _ in range(3):
            cube[i].append("B")

    for i in range(3):
        print(' '*9, end='')
        for j in range(3):
            print(cube[i][j], end=' ')
        print()
cube1 = [[] for _ in range(3)]
matrix_B(cube1)

def matrix_W(cube):
    for i in range(3):
        for _ in range(3):
            cube[i].append("W")

    for i in range(3):
        for j in range(3):
            print(cube[i][j], end=' ')
        print()
cube2 = [[] for _ in range(3)]
matrix_W(cube2)

