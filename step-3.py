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

def read_command(rcmd):
    i=0
    while True:
        cmd = rcmd
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
            Q(1)
        i += 2

while 3:
    usrInput = input("CUBE=> ").upper()
    command = list(usrInput)

    def command_change(cmd):
        for i in range(0, len(cmd), 2):
            if len(cmd)==1:
                break
            elif cmd[i+1] == '\"':
                cmd[i+1] = '+'
            else:
                cmd.insert(i+1, '-')

        if cmd[-1] == '\"':
            cmd[-1] = '+'
        else:
            cmd.append('-')
        read_command(cmd)
        
    command_change(command)

    def clockWise(cube):
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
        
        
