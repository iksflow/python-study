# FourCal 클래스를 정의
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

# FourCal의 인스턴스인 객체 a 생성
a = FourCal()

# a의 타입 확인
print(type(a))

# FourCal의 인스턴스 a로 setdata 메서드를 호출
a.setdata(4, 2)
print("a.first = ", a.first)
print("a.second = ", a.second)
# Fourcal을 통해 setdata를 호출하는것도 가능
FourCal.setdata(a, 5, 3)
print("a.first = ", a.first)
print("a.second = ", a.second)
print("a.add() = ", a.add())
print("a.mul() = ", a.mul())
print("a.sub() = ", a.sub())
print("a.div() = ", a.div())

# setdata 없이 add 호출
b = FourCal()
# first, second가 초기화되지 않았으므로 오류가 발생한다
# b.add()

# setdata를 사용하기 보단 생성자를 통해 객체 생성시 값을 할당하는게 안전하다.
# __init__ 메서드를 정의한 순간 기존의 FourCal()은 인자가 모자른 호출이 되므로 오류를 발생시킨다