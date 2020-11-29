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

## 매개변수 지정해서 호출하기
def printAThenB(a, b):
    return "%s then %s" % (a, b)

print("printAThenB(3,7) =", printAThenB(3, 7))
print("printAThenB(b=7, a=3)", printAThenB(b=7, a=3))

## 인자가 여러개 있을경우
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
print("add_many(1,2,3) = ", add_many(1,2,3))
print("add_many(1,2,3,4,5,6) = ", add_many(1,2,3,4,5,6))

# 키워드 파라미터

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
