# 튜플

# 단일요소 튜플
noTuple = (1)
tuple = (1,)
# 뒤에 콤마를 안붙이면 정수로 인식해버린다. 단일 요소 튜플을 표현할 때는 반드시 뒤에 ',' 를 붙여야한다.
print("noTuple : ", noTuple)
print("tuple : ", tuple)
# 튜플 정의하기
t1 = (1, 2, 'a', 'b')
t2 = 1, 2, 'a', 'b'
print("t1 : ", t1)
print("t2 : ", t2)

# 튜플 요소 삭제하기 (오류 발생)
# del t1[0]

# 튜플 요소 변경하기 (오류 발생
# t1[0] = 3

# 인덱싱
print("t1[0] : ", t1[0])

# 슬라이싱
print("t1[:2] : ", t1[:2])

# 튜플 더하기
t3 = (1, 2, 'a', 'b')
t4 = (3, 4)
print("t3 : ", t3)
print("t4 : ", t4)
print("t3 + t4 = ", t3 + t4)

# 튜플 곱하기
t5 = (1, 2, 'a')
print("t5 * 2 = ", t5 * 2)

# 튜플 길이구하기
t6 = (1, 2, 3, 4, 5)
print("t6 : ", t6)
print("len(t6) = ", len(t6))