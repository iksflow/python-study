# 함수

# 함수를 정의하는 방법
def add(a, b):
    return a + b
print("add(3, 4) = ", add(3, 4))


# 입력값이 없는 함수
def sayHi():
    print("Hi Python!")
sayHi()

# 결과값이 없는 함수 출력하면 반환값이 None으로 나옴
def addNumberThenPrint(a, b):
    print("%d + %d = %d" %(a, b, a+b))
print(addNumberThenPrint(3, 4))