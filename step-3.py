def matrix_6x3x3(cube):

    color_str="BWOGYR"
    for i in range(6):
        for j in range(3):
            for _ in range(3):
                cube[i][j].append(color_str[i])

    for i in range(1):
        for j in range(3):
            print(' '*15, end='')
            for k in range(3):
                    print(cube[i][j][k], end=' ')
            print()
    print()
    
    for i in range(1, 5):
        for j in range(1):
            if i != 1:
                print(' '*4, end='')
            for k in range(3):
                print(cube[i][j][k], end=' ')
    if cube[i][j][k] == cube[4][0][2]:
        print()
            
    for i in range(1, 5):
        for j in range(1, 2):
            if i != 1:
                print(' '*4, end='')
            for k in range(3):
                print(cube[i][j][k], end=' ')
    if cube[i][j][k] == cube[4][0][2]:
        print()

    for i in range(1, 5):
        for j in range(2, 3):
            if i != 1:
                print(' '*4, end='')
            for k in range(3):
                print(cube[i][j][k], end=' ')
    if cube[i][j][k] == cube[4][0][2]:
        print()

    for i in range(5, 6):
        print()
        for j in range(3):
            print(' '*15, end='')
            for k in range(3):
                    print(cube[i][j][k], end=' ')
            print()
        
cube = [[[] for _ in range(3)]for _ in range(6)]
matrix_6x3x3(cube)
