## 루빅스 큐브 프로그래밍 3단계  

1. 6x3x3의 6color 큐브 생성 **[Commit No.1]**    
- list([]) 안에 [] * 3EA 생성 // 각 list 마다 element 3개씩들어갈 공간  
- 이러한 list를 6EA 생성 // 6color가 모두 들어가야 하기 때문 => 6x3x3 큐브생성완료  
2. 각 색깔별로 3x3 Matrix를 print 하는 함수로 수정 **[Commit No.2]**    
- 6x3x3의 3차원 배열에서 주어진 모양의 큐브를 print하기 어려워 각 함수별로 코드 수정  
- B와 W까지 진행하면서 이런 방식으로는 큐브의 초기 형태를 print할 수는 있어도, step-2에서 구축한 코드사용은 불가  
- Commit No.1으로 코드 돌아가서 다시 print 함수 제작  
3. 6x3x3 형태의 큐브를 펼친상태로 Print하기 **[Commit No.3]**  
- 해당 코드를 짜보면서 for문에 대한 이해도가 비약적으로 높아짐  
- 파이썬의 경우 " end='' " 기능을 활용하여 줄바꿈을 하지 않을 수 있는데, 이 기능을 이용하여 W, O, G,Y 줄바꿈을 하지 말아야함  
- 하지만 문제점은 B B B와 같이 3[인덱스로는 2]번째에서 줄바꿈은 필수인데, 이렇게 줄바꿈을 할경우 W, O, G, Y에서도 줄이 바뀜
- Step-1과 Step-2를 해결하는데 아마 2시간정도 걸렸는데, 지금 Step-3 큐브의 초기상태 print하는데 2시간 걸려서도 실패  
4. 큐브의 초기 상태 Print 성공 **[Commit No.4]**      
- 퇴근 후, 2시간 동안 print시도하였으나 실패 => 아침 출근길에 for문을 나눠서 각자 출력하면 가능할까 싶어서 시도  
- B와 R은 한번에 3x3형태로 출력하고, 문제가됐던W,O,G,Y를 각 color별로가 아닌 인덱스 별로 print()  
- 예를들면 [1][0][0] ~ [4][0][2] // [1][1][0] ~ [4][1][2] // [1][2][0] ~ [4][2][2] 로 출력
- 마침내 큐브의 초기상태 print() 성공 => 단, 이 방법이 유일하지 않은 것 같은데 조금 더 효율적은 코드는 아직 모르겠음    
5. UserInput값을 받기 위한 While-loop 및 해당 값을 읽기 위한 함수 제작 **[Commit No.5]**        
- Step-2에서 사용했던 UserInput값을 받기 위한 코드를 While-loop 안으로 이동 => Q값을 받을 때까지 반복하기 위함  
- 해당 While-loop는 현재 3(임시적으로), 이후 True로 수정하여 Q함수가 실행되면 프로그램 종료되도록 설계예정  
- UserInput값을 받아서 각 함수로 전달하는 read_command 함수도 제작 => 마찬가지로 Step-2 코드 그대로 활용    
6. Command에 따라 움직일 각 면에 대한 공통 Clockwise function 구축 **[Commit No.6]**  
- Step-2에서 사용했던 코드를 재구현하기 전에, 공통적으로 사용할 시계방향 회전 함수 구축  
- 각 색깔별 함수가 돌아갈때마다 clockwise 함수를 먼저 해당 면에 대해 돌리면 매번 코드짤 필요가 없음  
- 필요할 때 마다 각 면(해당 면에 대한 Cube의 인덱스)을 제공받을 예정이기 때문에 [0][0][0]이 아니라, [0][0]형태로 구축    
7. Command (U)가 입력됐을 때, 시계 방향으로 K만큼 회전하는 함수 구축 **[Commit No.7]**  
- 시계 방향, 반시계 방향은 구분할 필요 없이 => 반시계 방향으로 입력됐을 때 시계방향x3 이동하면 동일한 결과
- read_command 함수에서 시계방향 반시계방향 읽어서 시계방향이면 1, 반시계방향이면 3을 변수 K로 전달
- 이후 F,R,B,L,D에 대해서는 한번에 구축 후에 Commit할 예정  
8. Command (U, L, F, R, B, D) 별로 시계 방향으로 K만큼 회전하는 함수 구축 **[Commit No.8]**
- 큐브 초기상태를 print할 때, 완성된 큐브를 펼치는 형식이 아니라 평면 큐브를 펼치는 식으로 print
- 따라서, index 교체하는데 시간이 오래 걸림(하나하나 큐브 돌아가는거 생각하면서 인덱스 교체 코딩)  
9. UserInput 값 Q 받으면 프로그램 종료기능 추가, 하지만 원점으로 **[Commit No.9]**  
- Q를 입력값으로 받으면 프로그램 종료기능 추가 및 rotation function 기능 정상작동 확인  
- 하지만 인덱스로 element요소 변경하면서 print() 찍히는 위치가 달라짐  
- 이로 인하여 큐브를 돌리다보면 초기 큐브 형태대로 print되는 것이 아니라 형태가 무너짐  
- 결국 큐브 초기형태 print하는 코드 수정이 필요함 => 다시 원점  
- 기타 추가 기능 및 숫자입력시 숫자만큼 rotation하는 기능 추가해야함  
10. 기존 CUBE 생성 및 초기형태 print 함수를 각 기능별로 2개로 분리 **[Commit No.10]**  
- 기존 코드는 CUBE 생성 및 초기형태 print 함수가 하나였으나, 각 기능별로 분리
- 큐브 돌리면서 초기형태가 무너지는 에러 원인을 찾기 위해 print함수 코드 수정
- 초기형태 유지하지 않고 평면 큐브 형태로 print하니 문제 없이 rotation 기능 작동
- 큐브돌리면서 기능 정상 작동하는 지 확인 중, D rotation 함수에서 오류 발견하고 수정
- 현재 필요한 기능 => 1. 초기상태print(수정) // 2. 작동 횟수(추가) // 3. UserInput 숫자읽기(작업중) // 구동시간(추가)
11. UserInput 값(command)를 정확하게 읽을 수 있도록 코드 수정 완료 **[Commit No.11]**  
- e.g.) 숫자 및 ' 입력시 알파벳 또는 -, +로 변경하여 rotation 돌 수 있도록 코드 수정 완료
- 숫자값을 isdigit으로 읽기위해서 userInput에서 upper()제거하고 command읽는 while-loop에 소문자 추가완료
- 기존 for-loop사용시 고려하지 못하여 idx나 입력되는 UserInput에 따라 -나 +를 추가하지 못하는 부분 While문으로 수정하면서 수정완료
- 현재 필요한 기능 => 1. 초기상태print(수정) // 2. 작동 횟수(추가) // 3. UserInput 숫자읽기(2외에 숫자 읽는 방향 추가필요) // 구동시간(추가)  
12. 숫자가 입력됐을 때 숫자만큼 알파벳으로 전환할 수 있도록 코드 수정 완료 **[Commit No.12]**  
- UserInput 값 중 숫자가 입력됐을 때 숫자만큼 알파벳으로 전환하여 rotation함수로 전달할 수 있도록 수정완료
- 현재 필요한 기능 => 1. 초기상태print(수정) // 2. 작동 횟수(추가) // 3. 구동 시간(추가)
13. 작동 횟수 및 구동시간 기능 추가 완료 **[Commit No.13]**  
- 작동 횟수 variable cnt 생성하여 command를 rotation으로 전달할 때마다 cnt+=1로 카운팅 완료
- 작동시간 end time - start time 으로 구현 완료 => 00:00 형태로 수정 해야 함
- 현재 필요한 기능 => 초기상태print(수정) // 2. 구동시간(수정)  
14. 구동시간 00:00 형태로 수정 완료 **[Commit No.14]**
- 7.1249초로 나오는 시간 timedelta 없이 %60, //60으로 초, 분으로 수정완료
- 현재 필요한 기능 => 초기상태print(수정)  
15. 프로그래밍 완료 **[Commit No.15]**
- 초기 큐브 형태 print() 성공
- command값대로 rotation 돌려도 초기 큐브 형태 무너지지 않음
- 기존에 print()값으로 공백 만드는 위치를 잘못선정하여 if cube[i][j][k] == cube[4][0][2]: 와 같은 코드가 문제였음  
- 해당 코드 제거하고 올바른 위치에 print() 넣는 것만으로 오류 수정완료

매일 코딩테스트만 연습하다보니 간단한 프로그램 제작은 처음이었는데,  
하나하나 코드짜넣고 실행해가면서 오류를 찾고 결국 완성을 했다.    
알게모르게 성취감도 크고 그냥 알고리즘이나 코딩테스트 공부하는 것보다    
코딩 실력이 확실히 많이 늘었다.  
확실히 코딩 공부도 자기주도적으로 실패해가면서 배우는게 좋은 것 같다.  
다만, 코드리뷰하면서 내 실력으로는 생각하기 어려운 refactorying과정에 대해  
피드백 받고 코드를 수정해가지 못하는 점이 혼자 공부하는 것의 한계일듯 싶다.  
