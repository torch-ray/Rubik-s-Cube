def cube_plane(cube):
    for i in range(6):
        print()
        for j in range(3):
            for k in range(3):
                print(cube[i][j][k], end=' ')
            print()
    print()

def matrix_6x3x3(cube):

    color_str="BWOGYR"
    for i in range(6):
        for j in range(3):
            for _ in range(3):
                cube[i][j].append(color_str[i])
    cube_plane(cube)
    
cube = [[[] for _ in range(3)]for _ in range(6)]
matrix_6x3x3(cube)

while True:
    exitLoop=False

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
            cube[1][2][0], cube[1][2][1], cube[1][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
            cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[3][2][0], cube[3][2][1], cube[3][2][2]
            cube[3][2][0], cube[3][2][1], cube[3][2][2] = cube[2][2][0], cube[2][2][1], cube[2][2][2]
            cube[2][2][0], cube[2][2][1], cube[2][2][2] = tmp
            print("D")
            matrix_6x3x3(cube)

    usrInput = input("CUBE=> ")
    print()
    command = list(usrInput)
    
    cmd1=[]
    while command:
        if command[0].isalpha() == True:
            cmd1.append(command.pop(0))
            cmd1.append('-')
        elif command[0].isdigit() == True:
            for i in range(int(command[0])-1):
                cmd1.append(cmd1[-2])
                cmd1.append('-')
            command.pop(0)
        else:
            cmd1.pop()
            cmd1.append('+')
            command.pop(0)
    print(cmd1)
    i=0
    while True:
        cmd = cmd1
        if i > len(cmd)-2:
            break

        if cmd[i] == "F" or cmd[i] == "f":
            if cmd[i+1] == '+':
                F(3)
            else:
                F(1)
        elif cmd[i] == "R" or cmd[i] == "r":
            if cmd[i+1] == '+':
                R(3)
            else:
                R(1)
        elif cmd[i] == "U" or cmd[i] == "u":
            if cmd[i+1] == '+':
                U(3)
            else:
                U(1)
        elif cmd[i] == "B" or cmd[i] == "b":
            if cmd[i+1] == '+':
                B(3)
            else:
                B(1)
        elif cmd[i] == "L" or cmd[i] == "l":
            if cmd[i+1] == '+':
                L(3)
            else:
                L(1)
        elif cmd[i] == "D" or cmd[i] == "d":
            if cmd[i+1] == '+':
                D(3)
            else:
                D(1)
        elif cmd[i] == "Q" or cmd[i] == "q":
            print("이용해주셔서 감사합니다. 뚜뚜뚜.")
            exitLoop=True
            break
        i += 2
    
    if exitLoop == True:
        break

