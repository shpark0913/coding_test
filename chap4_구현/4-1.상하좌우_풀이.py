# 공간의 크기 (N by N matrix)
N = int(input())

# 여행자가 이동할 계획서
moveList = list(input().split())

# 여행자의 위치를 담는 변수
location = [1, 1]


for move in moveList:
    if move == "L": move = [0, -1]
    elif move == "R": move = [0, 1]
    elif move == "U": move = [-1, 0]
    else: move = [1, 0]
    for i in range(2):
        if location[i] + move[i] > 0:
            location[i] += move[i]

print(*location)