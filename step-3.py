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



while True:
    x=False
    def clockWise(arr):
        tmp = arr[0][0]
        arr[0][0] = arr[0][2]
        arr[0][2] = arr[2][2]
        arr[2][2] = arr[2][0]
        arr[2][0] = tmp

        tmp = arr[0][1]
        arr[0][1] = arr[1][2]
        arr[1][2] = arr[2][1]
        arr[2][1] = arr[1][0]
        arr[1][0] = tmp

    def U(k):
        for _ in range(k):
            clockWise(cube[0])
            tmp = cube[1][0][0], cube[1][0][1], cube[1][0][2]
            cube[1][0][0], cube[1][0][1], cube[1][0][2] = cube[2][0][0], cube[2][0][1], cube[2][0][2]
            cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
            cube[3][0][0], cube[3][0][1], cube[3][0][2] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
            cube[4][0][0], cube[4][0][1], cube[4][0][2] = tmp
            print("U")
            matrix_6x3x3(cube)
            

    def L(k):
        for _ in range(k):
            clockWise(cube[1])
            tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[4][2][2], cube[4][1][2], cube[4][0][2]
            cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
            cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[2][2][0], cube[2][1][0], cube[2][0][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = tmp
            print("L")
            matrix_6x3x3(cube)

    def F(k):
        for _ in range(k):
            clockWise(cube[2])
            tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[1][2][2], cube[1][1][2], cube[1][0][2]
            cube[1][2][2], cube[1][1][2], cube[1][0][2] = cube[5][0][2], cube[5][0][1], cube[5][0][0]
            cube[5][0][2], cube[5][0][1], cube[5][0][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = tmp
            print("F")
            matrix_6x3x3(cube)

    def R(k):
        for _ in range(k):
            clockWise(cube[3])
            tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[5][0][2], cube[5][1][2], cube[5][2][2]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
            cube[4][2][0], cube[4][1][0], cube[4][0][0] = tmp
            print("R")
            matrix_6x3x3(cube)

    def B(k):
        for _ in range(k):
            clockWise(cube[4])
            tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[5][2][2], cube[5][2][1], cube[5][2][0]
            cube[5][2][2], cube[5][2][1], cube[5][2][0] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
            cube[1][2][0], cube[1][1][0], cube[1][0][0] = tmp
            print("B")
            matrix_6x3x3(cube)

    def D(k):
        for _ in range(k):
            clockWise(cube[5])
            tmp = cube[1][2][0], cube[1][2][1], cube[1][2][2]
            cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[4][1][0], cube[4][2][1], cube[4][2][2]
            cube[4][1][0], cube[4][2][1], cube[4][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
            cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][2][0], cube[2][2][1], cube[2][2][2]
            cube[2][2][0], cube[2][2][1], cube[2][2][2] = tmp
            print("D")
            matrix_6x3x3(cube)
            
    usrInput = input("CUBE=> ").upper()
    command = list(usrInput)
    
    for i in range(0, len(command), 2):
            if len(command)==1:
                break
            elif command[i+1] == '\"':
                command[i+1] = '+'
            else:
                command.insert(i+1, '-')

    if command[-1] == '\"':
        command[-1] = '+'
    else:
        command.append('-')
            

    i=0
    while True:
        cmd = command
        if i > len(cmd)-2:
            break

        if cmd[i] == "F":
            if cmd[i+1] == '+':
                F(3)
            else:
                F(1)
        elif cmd[i] == "R":
            if cmd[i+1] == '+':
                R(3)
            else:
                R(1)
        elif cmd[i] == "U":
            if cmd[i+1] == '+':
                U(3)
            else:
                U(1)
        elif cmd[i] == "B":
            if cmd[i+1] == '+':
                B(3)
            else:
                B(1)
        elif cmd[i] == "L":
            if cmd[i+1] == '+':
                L(3)
            else:
                L(1)
        elif cmd[i] == "D":
            if cmd[i+1] == '+':
                D(3)
            else:
                D(1)
        elif cmd[i] == "Q":
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            x=True
            break
        i += 2
    
    if x == True:
        break
    
