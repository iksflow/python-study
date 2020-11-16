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
# e = a - b
# print(e)
print("len(a) = ", len(a))

# 리스트 값 수정
list1 = [1, 2, 3, 4]
list1[0] = 5
print("list1 : ", list1)

# 리스트 요소 삭제하기
list2 = [1, 3, 5, 7]
del list2[0]
print("del list2[0] / list2 : ", list2)

# 리스트 요소 슬라이싱해서 삭제하기
list3 = [1, 2, 3, 4, 5]
del list3[:3]
print("del list3[:3] / list3 : ", list3)

# 리스트에 요소 추가하기
list4 = [1, 2, 3]
list4.append(4)
list4.append([5, 6])
print("list4 : ", list4)

# 리스트 정렬

list5 = [4, 1, 2, 3]
# 오름차순으로 정렬
list5.sort()
print("list5.sort() : ", list5)
# 거꾸로 정렬 (내림차순정렬이 아님)
list5.reverse()
print("list5.reverse() : ", list5)
# 리스트 정렬 (다른 자료형이 껴있으면 오류 발생)
# list6 = [4, 1, 2, 3, 'a']
# list6.sort()
# print("list6.sort() : ", list6)

# 리스트 내 특정 값의 인덱스 반환

list7 = [1, 2, 3, 4, 1]
print("list7.index(4) : ", list7.index(4))
# 5란 값이 존재하지 않으므로 오류 발생
# print("list7.index(5) : ", list7.index(5))
# 특정 값이 리스트 내에 여러개 있을 경우 가장 작은 인덱스를 반환함
print("list7.index(1) : ", list7.index(1))


# 리스트에 요소 삽입(insert)

list8 = [1, 2, 3, 4]
# index=2 인 자리에 7이란 값을 삽입
list8.insert(2, 7)
print("list8.insert(2, 7)", list8)
# 뒤에서 두번째 요소에 7이란 값을 삽입
list8.insert(-1, 7)
print("list8.insert(-1, 7)", list8)
# 초과하는 인덱스에 값을 삽입 (맨 끝에 삽입됨)
list8.insert(999, 7)
print("list8.insert(999, 7)", list8)

# 리스트 요소 꺼내기(pop)

list9 = [1, 2, 3, 4]
# 인자가 없으면 맨 마지막 요소를 꺼냄
print("list9.pop() : ", list9.pop())
print("list9 : ", list9)
# 리스트의 x번째 요소를 꺼낸다
# [1,2,3] 의 2번째요소인 3을 꺼냄. (0,1,2 순서이므로)
print("list9.pop(2) : ", list9.pop(2))
print("list9 : ", list9)


# 리스트에 포함된 요소x의 개수 세기(count)

list10 = [1, 2, 3, 4, 1, 1]
# 인자를 전달하지 않으면 오류 발생
# print("list10.count()", list10.count())
print("list10.count(1) : ", list10.count(1))


# 리스트 확장(extend)

# extend는 인자로 리스트를 받으며 맨 뒤로 인자를 이어붙인다.
list11 = [1, 2, 3]
list11.extend([4, 5])
print("list11 : ", list11)
# extend와 += 연산은 같다.
list11 += [6, 7]
print("list11 : ", list11)