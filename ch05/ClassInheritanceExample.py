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

# class 클래스이름(상속할 클래스 이름)의 방식으로 상속할 클래스를 정한다. 상속할 클래스는 자식클래스보다 먼저 정의되어야한다.
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = MoreFourCal(4, 2)
print("a.add() = ", a.add())
print("a.mul() = ", a.mul())
print("a.sub() = ", a.sub())
print("a.div() = ", a.div())
print("a.pow() = ", a.pow())
b = SafeFourCal(4, 0)
# overriding 된 함수가 호출된다.
print("b.div() = ", b.div())

# 클래스변수 정의하기
class Family:
    lastname = "김"

# 클래스를 통해 호출하는 방법
print("Family.lastname =", Family.lastname)
f1 = Family()
f2 = Family()
# 인스턴스를 통해 호출하는 방법
print("f1.lastname = ", f1.lastname)
print("f2.lastname = ", f2.lastname)

# 클래스 변수 값 변경하기
Family.lastname = "박"

# 생성된 모든 객체의 lastname이 변경됐다.
print("f1.lastname = ", f1.lastname)
print("f2.lastname = ", f2.lastname)

# id로 비교해보면 같은 메모리주소를 참조하고있는것을 알 수 있다.
print("id(f1.lastname) = ", id(f1.lastname))
print("id(f2.lastname) = ", id(f2.lastname))