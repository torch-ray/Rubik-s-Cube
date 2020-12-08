def matrix_6x3x3(cube):

    color_str="BWOGYR"
    for i in range(6):
        for j in range(3):
            for _ in range(3):
                cube[i][j].append(color_str[i])

    for i in range(6):
        print()
        for j in range(3):
            if i==0 or i==5:
                print(' '*15, end='')
            elif i==2:
                print(' '*10, end='')
            elif i==3:
                print(' '*21, end='')
            elif i==4:
                print(' '*32, end='')
            for k in range(3):
                print(cube[i][j][k], end=' ')
            print()
            
    
cube = [[[] for _ in range(3)]for _ in range(6)]
matrix_6x3x3(cube)
