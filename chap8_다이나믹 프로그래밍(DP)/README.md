## 다이나믹 프로그래밍(Dynamic Programming)
- 동적 계획법
- 메모리 공간을 약간 더 사용하면 연산 속도를 비약적으로 증가시킬 수 있음
- 탑다운, 보텀업 방식이 있음
- 다이나믹
  - "프로그램이 실행되는 도중에" 라는 의미

## 피보나치 수열
- DP의 대표적인 예시
- n번째 피보나치 수 = (n - 1)번째 피보나치 수 + (n - 2)번째 피보나치 수
- 1번째 피보나치 수 = 1, 2번째 피보나치 수 = 1

## DP를 사용할 수 있는 경우
1. 큰 문제를 작은 문제로 나눌 수 있다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

## 메모이제이션
- DP를 구현하는 방법 중 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
- 값을 저장하는 방법이므로 캐싱(Caching)이라고도 함

## 다이나믹 프로그래밍이란?
- 큰 문제를 작게 나누고, 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘

### 탑다운 방식
- 큰 문제를 해결하기 위해 작은 문제를 호출하는 방식

### 보텀업 방식
- 반복문을 이용해 소스코드를 작성하는 경우
- 작은 문제부터 차근차근 답을 도출하는 방식