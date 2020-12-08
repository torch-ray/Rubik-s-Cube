import os

def matrix_3x3(arr):
       for i in range(3):
              for j in range(3):
                     print(cube[i][j], end=' ')
              print()
              
cube=[["R", "R", "W"], ["G", "C", "W"], ["G", "B", "B"]]
matrix_3x3(cube)
print()


usrInput = input("CUBE => ")
print()
       
command = list(usrInput)

for i in range(0, len(command), 2):
       if len(command) == 1:
              break
       elif command[i+1] == '\'':
              command[i+1] = '+'
       else:
              command.insert(i+1, '-')
if command[-1] == '\'':
       command[-1] = '+'
else:
       command.append('-')
       
def U(k):

       for _ in range(k):
              tmp=cube[0][0]
              cube[0][0]=cube[0][1]
              cube[0][1]=cube[0][2]
              cube[0][2]=tmp
              print("U")
              matrix_3x3(cube)
              print()

def R(k):

       for _ in range(k):
              tmp=cube[0][2]
              cube[0][2]=cube[1][2]
              cube[1][2]=cube[2][2]
              cube[2][2]=tmp
              print("R")
              matrix_3x3(cube)
              print()

def L(k):

       for _ in range(k):
              tmp=cube[0][0]
              cube[0][0]=cube[2][0]
              cube[2][0]=cube[1][0]
              cube[1][0]=tmp
              print("L")
              matrix_3x3(cube)
              print()

def B(k):

       for _ in range(k):
              tmp=cube[2][0]
              cube[2][0]=cube[2][2]
              cube[2][2]=cube[2][1]
              cube[2][1]=tmp
              print("B")
              matrix_3x3(cube)
              print()
i=0
while True:
       cmd = command
       if i > len(cmd)-2:
              break
       
       if cmd[i] == "U" or "u":
              if cmd[i+1] == '+':
                     U(2)
              else:
                     U(1)
       elif cmd[i] == "R" or "r":
              if cmd[i+1] == '+':
                     R(2)
              else:
                     R(1)
       elif cmd[i] == "L" or "l":
              if cmd[i+1] == '+':
                     L(2)
              else:
                     L(1)
       elif cmd[i] == "B" or "b":
              if cmd[i+1] == '+':
                     B(2)
              else:
                     B(1)
       elif cmd[i] == "Q":
              print("Bye~")
              print()
              break
       i += 2

os.system("pause")   
