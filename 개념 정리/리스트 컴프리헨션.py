# 20 이하의 홀수들로 구성된 리스트를 만들어보자.
array = []

for i in range(20):
    if i % 2:
        array.append(i)
# =>
array_list_comprehension = [i for i in range(20) if i % 2]


# 1부터 9까지의 수의 제곱 값을 포함하는 리스트를 만들어보자.
array_square = []

for i in range(1, 10):
    array_square.append(i ** 2)
# =>
array_square_list_comprehension = [i ** 2 for i in range(1, 10)]

# 리스트 컴프리헨션은 "2차원 리스트를 초기화할 때 매우 효과적"이다.
# 사실, 특정 크기의 2차원 리스트를 초기화할 때는 반드시 리스트 컴프리헨션을 이용해야 한다!!!!!!
# N X M  크기의 2차원 리스트를 초기화할 때 =>
N, M = 3, 4
array_example = [[0] * M for _ in range(N)]
