## 루빅스 큐브 프로그래밍 3단계  
1. 6x3x3의 6color 큐브 생성[Commit No.1]    
- list([]) 안에 [] * 3EA 생성 // 각 list 마다 element 3개씩들어갈 공간  
- 이러한 list를 6EA 생성 // 6color가 모두 들어가야 하기 때문 => 6x3x3 큐브생성완료  
2. 각 색깔별로 3x3 Matric를 print 하는 함수로 수정[Commit No.2]  
- 6x3x3의 3차원 배열에서 주어진 모양의 큐브를 print하기 어려워 각 함수별로 코드 수정  
- B와 W까지 진행하면서 이런 방식으로는 큐브의 초기 형태를 print할 수는 있어도, step-2에서 구축한 코드사용은 불가  
- Commit No.1으로 코드 돌아가서 다시 print 함수 제작
