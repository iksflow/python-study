from copy import copy

a = [1, 2, 3]
# a의 메모리주소
print("id(a) = ", id(a))

# 리스트의 복사 : 주소의 복사가 일어난다.
b = a
print("id(a) = ", id(a))
print("id(b) = ", id(b))

# a와 b가 정말로 같은객체인지 확인해보자
print("a is b = ", a is b)

# a의 값을 바꾸는경우 b도 바뀐다
a[1] = 4
print("a : ", a)
print("b : ", b)

# a와 b는 얕은 복사(shallow copy)가 되었기 때문에 서로 같은 객체를 공유하고 있다.
# 그러면 내용이 같은 다른 객체를 생성하려면 어떻게할까?
c = [1, 2 ,3]

# 1. [:] 전체 슬라이싱
c1 = c[:]
# 2. copy 모듈 사용
c2 = copy(c)

# 서로 다른객체가 생성된것을 확인할 수 있다.
print("c is c1 = ", c is c1)
print("c is c2 = ", c is c2)
print("c1 is c2 = ", c1 is c2)


# 변수를 생성하는 여러가지 방법
a1, b1 = ('python', 6)
print("a1 : ", a1, "/ b1 : ", b1)
# 두 변수의 값 바꾸기
a1, b1 = b1, a1
print("a1 : ", a1, "/ b1 : ", b1)

