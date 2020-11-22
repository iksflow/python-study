# 불 자료형 True, False를 나타냄

a = True
b = False
print("type(a) = ", type(a))
print("type(b) = ", type(b))

# 조건문의 반환 값
print("1 == 1 = ", 1 == 1)
print("2 < 1 = ", 2 < 1)

# 자료형의 참과 거짓
a = [1, 2, 3, 4]

# a의 요소가 들어있는 경우 True를 반환함. 따라서 a에 요소가 남아있지 않게되면 반복문을 빠져나오게된다.
# [1, 2, 3...] = True, [] = False
while a:
    print(a.pop())

# 튜플의 경우도 리스트와 마찬가지이다.
# (1, 2, 3...) = True, () = False
if ():
    print("True")
else:
    print("False")

# bool 함수를 사용해 자료형 bool값 확인하기
print("bool('') = ", bool(''))
print("bool('python') = ", bool('python'))
print("bool(1) = ", bool(1))
print("bool(0) = ", bool(0))


