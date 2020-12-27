class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)
print("cal.value =", cal.value)

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        self.value = min(100, self.value)

cal2 = MaxLimitCalculator()
cal2.add(50)
cal2.add(60)
print(cal2.value)

print(all([1, 2, abs(-3)-3]))
print(chr(ord('a')) == 'a')


print(list(filter(lambda x: x > 0, [1, -2, 3, -5, 8, -3])))
print(int(hex(234), 16))