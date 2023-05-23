N = int(input())

electronics = sorted(list(map(int, input().split())))

M = int(input())

wonders = sorted(list(map(int, input().split())))

for wonder in wonders:
    if wonder in electronics:
        print('yes')
    else:
        print('no')