numInput = int(input("원하시는 프로그램 실행 횟수를 입력해주세요 : "))
for _ in range(numInput):
    usrInput = input('단어, 정수, L 또는 R을 공백과 함께 입력하세요 : ').split()

    word = usrInput[0]
    num = int(usrInput[1])
    direc = usrInput[2].upper()
    arr = list(word)

    if num < 0:
        if direc == "L":
            direc = "R"
        else:
            direc = "L"

    for i in range(abs(num)):
        if direc == "L":
            arr.append(arr.pop(0))
        else:
            arr.insert(0, arr.pop(-1))
            
    print(''.join(arr))

