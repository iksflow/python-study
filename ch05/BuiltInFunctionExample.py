# 내장함수

# abs(x) 절대값구하기
print("abs(-3) =", abs(-3))

# all(x) iterable 자료형을 인수로 받음. 인수의 요소가 전부 참인경우 True, 거짓이 하나라도 있으면 False
print("all([1, 2, 3]) =", all([1, 2, 3]))
print("all([1, 2, 3, 0]) =", all([1, 2, 3, 0]))

# any(x) all과 달리 인수의 요소 중 1개라도 True가 있다면 True를 반환함
print("any([0, 0, 0]) =", any([0, 0, 0]))
print("any([0, 0, 3, 0]) =", any([0, 0, 3, 0]))

# chr(x) 인수로 아스키코드값을 전달하면 대응되는 문자를 반환한다.
print("chr(97) =", chr(97))

# dir(x) 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
print("dir([1,2,3]) =", dir([1,2,3]))
print("dir('hi') =", dir("hi"))
print("dir({'1':'a'}) =", dir({'1':'a'}))

# divmod(a, b) 2개의 숫자를 인수로 받는다. a를 b로 나눈 몫과 나머지를 튜플로 반환한다.
print("divmod(3, 4) =", divmod(3, 4))