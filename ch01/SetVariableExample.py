# 집합 자료형 정의하기
s1 = set([1, 2, 3])
print("s1 : ", s1)

# 집합 자료형의 특징
# - 1. 순서가 없다. 인덱싱으로 값을 얻을 수 없다.
# - 2. 중복을 허용하지 않는다.
s2 = set("Hello")
print("s2 : ", s2)

# 인덱싱으로 값을 얻으려면 리스트 또는 튜플로 변환하면 된다.
s3 = set([1, 2, 3])
print("s3 : ", s3)
l1 = list(s3)
print("l1 : ", l1)
t1 = tuple(s3)
print("s1 : ", t1)

# 집합의 연산 (교집합, 합집합, 차집합)

# 교집합
s4 = set([1, 2, 3, 4, 5, 6])
s5 = set([4, 5, 6, 7, 8, 9])
print("s4 & s5 = ", s4 & s5)
print("s4.intersection(s5) = ", s4.intersection(s5))

# 합집합
print("s4 | s5 = ", s4 | s5)
print("s4.union(s5) = ", s4.union(s5))

# 차집합
print("s4 - s5 = ", s4 - s5)
print("s4.difference(s5) = ", s4.difference(s5))