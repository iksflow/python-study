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


a = MoreFourCal(4, 2)
print("a.add() = ", a.add())
print("a.mul() = ", a.mul())
print("a.sub() = ", a.sub())
print("a.div() = ", a.div())
print("a.pow() = ", a.pow())