import os

def matrix_3x3(arr):
       for i in range(3):
              for j in range(3):
                     print(cube[i][j], end=' ')
              print()
              
cube=[["R", "R", "W"], ["G", "C", "W"], ["G", "B", "B"]]
matrix_3x3(cube)

usrInput = input("CUBE => ")
command = list(usrInput)

def U(cmd):
       if cmd == '\'':
              k=2
       else:
              k=1
       for _ in range(k):
              tmp=cube[0][0]
              cube[0][0]=cube[0][1]
              cube[0][1]=cube[0][2]
              cube[0][2]=tmp
              print(cube)

def R(cmd):
       if cmd == '\'':
              k=2
       else:
              k=1
       for _ in range(k):
              tmp=cube[0][2]
              cube[0][2]=cube[1][2]
              cube[1][2]=cube[2][2]
              cube[2][2]=tmp
              print(cube)

def L(cmd):
       if cmd == '\'':
              k=2
       else:
              k=1
       for _ in range(k):
              tmp=cube[0][0]
              cube[0][0]=cube[2][0]
              cube[2][0]=cube[1][0]
              cube[1][0]=tmp
              print(cube)

def B(cmd):
       if cmd == '\'':
              k=2
       else:
              k=1
       for _ in range(k):
              tmp=cube[2][0]
              cube[2][0]=cube[2][2]
              cube[2][2]=cube[2][1]
              cube[2][1]=tmp
              print(cube)

while command:
       cmd = command.pop(0)
       if cmd[0] == "U":
              U(cmd[1])
       elif cmd[0] == "R":
              R(cmd[1])
       elif cmd[0] == "L":
              L(cmd[1])
       elif cmd[0] == "B":
              B(cmd[1])
       elif cmd[0] == "Q":
              print("Bye~")
              break
       
