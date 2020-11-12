# 문자열 정의하는 방법 4가지
a = "Hello Python"
b = 'Hello Python'
c = """Hello Python"""
d = '''Hello Python'''

print("\"Hello Python\" = " + a)
print("\'Hello Python\' = " + b)
print('"""Hello Python""" = ' + c)
print("'''Hello Python = '''" + d)

# 문자열의 연산
head = "Hello "
tail = "Python!"

# 더하기
print(head + tail)
# 빼기 는 오류난다.
# print(head - tail)
# print(head - 3)
# 곱하기
# 문자열간의 곱셈은 당연히 불가능
# print(head * tail)
# 문자열 * n은 문자열을 n만큼 반복한다.
# 음수의 경우 출력하는 문자열이 없으며
# 소수점의 경우 오류가 발생한다.

print("head * 3 = " + head * 3)
# print("head * 3 = " + head * 1.5)
# 나누기 불가
# print("head / 3 = " + head / 3)
# 나머지연산 불가
# print("head / 3 = " + head % 3)
print('=' * 50)

str1 = "hi" * 50
print(len(str1))
str2 = "Hello, Python!"
print(str2[0: ])
str3 = "I eat %s apples." % "five"
print(str3)
str4 = "I eat %s apples." % 5
print(str4)
right = "{0:>10}".format("hi")
print(right)
left = "{0:<10}".format("hi")
print(left)
center = "{0:^10}".format("hi")
print(center)
otherSpam = "{0:!^10}".format("hi")
print(otherSpam)