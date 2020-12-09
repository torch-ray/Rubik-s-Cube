## 루빅스 큐브 프로그래밍 3단계  

1. 6x3x3의 6color 큐브 생성 **[Commit No.1]**    
- list([]) 안에 [] * 3EA 생성 // 각 list 마다 element 3개씩들어갈 공간  
- 이러한 list를 6EA 생성 // 6color가 모두 들어가야 하기 때문 => 6x3x3 큐브생성완료  
2. 각 색깔별로 3x3 Matric를 print 하는 함수로 수정 **[Commit No.2]**    
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
