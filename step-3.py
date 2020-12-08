cube = [[[] for _ in range(3)]for _ in range(6)]
color_str="WBGYOR"

for i in range(6):
    for j in range(3):
        for _ in range(3):
            cube[i][j].append(color_str[i])
print(cube)
