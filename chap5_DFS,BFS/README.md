자료구조(Data Structure) : 데이터를 표현하고 관리하고 처리하기 위한 구조
  - 스택과 큐는 자료구조의 기초 개념으로, 다음의 두 핵심적인 함수로 구성
    - 삽입(Pusth) : 데이터를 삽입한다.
    - 삭제(Pop) : 데이터를 삭제한다.
    - 오버플로와 언더플로를 고민해야 한다.
      - Overflow : 특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산을 수행할 때 발생
      - Underflow : 특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생

스택(Stack)
  - 박스 쌓기
  - 선입후출 혹은 후입선출
  - 파이썬에서 스택 이용할 때는 별도의 라이브러리 사용할 필요가 없다.
    - 리스트에서 append()와 pop() 메서드 이용하면 스택 자료구조와 동일하게 동작한다

큐(Queue)
  - 대기 줄
  - 선입선출
  - 파이썬에서 큐 이용할 때는 collections 모듈에서 제공하는 deque 자료구조를 활용하자.
    - deque는 스택과 큐의 장점을 모두 채택함
    - 데이터를 넣고 뺴는 속도가 리스트 자료형에 비해 효율적
    - queue 라이브러리를 이요하는 것보다 더 간단
    - deque 객체를 리스트 자료형으로 변경하고자 한다면 list() 메서드 이용하자.
      - 5-2.큐_예제.py에서 list(queue) 를 하면 리스트 자료형이 반환됨.

재귀 함수
  - DFS, BFS 구현 위해 재귀 함수의 이해가 필요하다.
  - 자기 자신을 다시 호출하는 함수를 의미한다.
  - 재귀 함수의 종료 조건
    - 함수의 무한 호출 방지하기 위해 종료 조건을 꼭 명시해야 함.
  - 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용
    - 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
    - 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용하여 간편하게 구현될 수 있다.


그래프 표현 방식(인접 행렬 방식 vs 인접 리스트 방식)
- 메모리 측면
  - 인접 행렬
    - 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비됨
  - 인접 리스트
    - 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용
    - 하지만 연결된 데이터를 하나씩 확인해야 하기 때문에 특정한 두 노드가 연결되어 있는지 확인이 느림
      - 노드 1과 노드 7이 연결되어 있다면?
        - 인접 행렬 : graph[1][7] 만 확인
        - 인접 리스트 : 노드 1에 대한 인접 리스트를 앞에서부터 차례대로 확인
      - 따라서 특정한 노드와 연결된 모든 인접 노드를 순회한다면, 인접 리스트 방식이 인접 행렬에 비해 메모리 공간 낭비 적음

DFS
- 동작 과정
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다.
  2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
- 스택 자료구조에 기초한다는 점에서 구현이 간단하다.
- 실제로는 스택을 쓰지 않아도 되며, 탐색을 수행함에 있어 데이터의 개수가 N개인 경우 O(N)의 시간이 소요된다.

BFS
- DFS와 차이는?
  - DFS는 최대한 멀리 있는 노드 우선으로 탐색 / BFS는 반대
- BFS는 큐 자료구조를 이용하는 것이 정석.
- 동작 과정
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
  3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.
- 큐 자료구조에 기초한다는 점에서 구현이 간단하다.
  - deque 라이브러리를 사용하는 것이 좋으며, 탐색을 수행함에 있어 O(N)의 시간이 소요된다.
- 일반적으로 실제 수행 시간은 DFS보다 좋은 편이다.