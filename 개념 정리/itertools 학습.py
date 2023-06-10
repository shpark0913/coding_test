from itertools import permutations, combinations, product, combinations_with_replacement

data = ['A', 'B', 'C']

# 순열 구하기
result = list(permutations(data, 3))
print("순열", result)

# 조합 구하기
result2 = list(combinations(data, 3))
print("조합", result2)

# 중복순열 구하기
result3 = list(product(data, repeat=2))
print("중복순열", result3)

# 중복조합 구하기
result4 = list(combinations_with_replacement(data, 2))
print("중복조합", result4)