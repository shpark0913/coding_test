# O(N)
#   연산 횟수는 이동 횟수에 비례하므로.
# 시뮬레이션 유형
#   일련의 명령에 따라 개체를 차례대로 이동시키므로.
#########################################################

# 이동 횟수
n = int(input())

x, y = 1, 1

plans = input().split()

# L, R, U, D 에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)

#########################################################
# 배운 것.
#   1. 공백으로 쪼갠 input 값은 자동으로 list가 된다.
#       list(input().split()) -> input().split()
#   2. move_types 사용해서 index로 문제 풀기