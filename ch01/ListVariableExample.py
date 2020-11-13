a = [1, 2, 3]
print(a)
b = [1, '2', True]
print(b)
c = [a, b]
print(c)

# 리스트 인덱싱

# 첫번째 요소 반환
print(a[0])
# 마지막 요소 반환
print(a[-1])
# 요소의 요소 반환
print(c[1][2])

# 리스트 슬라이싱

# 전체 요소 리스트로 반환
print(a[:])
# 인덱스 i가 0<= i < 2 인 요소 반환
print(a[0:2])
# 인덱스 i가 0<= i 인 요소 반환
print(a[0:])
# 인덱스 i가 i < 2 인 요소 반환
print(a[:2])
# 중첩된 리스트의 슬라이싱
print(c[0][:1])

# 리스트 연산

# 더하기 : 두 리스트의 요소를 합침
d = a + b
print(d)

# 빼기 : 오류
e = a - b
print(e)
