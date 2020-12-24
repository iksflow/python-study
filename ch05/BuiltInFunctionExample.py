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

# enumerate(x) 리스트, 튜플, 문자열을 인수로 넘기면 인덱스 값을 포함하는 enumerate 객체를 반환한다.
enum1 = enumerate(['a', 'b', 'c'])
print(enum1.__next__())
print(enum1.__next__())

# eval(x) 실행 가능한 문자열을 입력받아 문자열을 실행한 결과값을 반환한다.
print(eval('1+2'))
print(eval('1+--2'))
hi = 'hello'
a = 'world'
print(eval('hi + a'))
print(eval('enum1.__next__() * 3'))

# filter(a, b) a는 함수, b는 리스트 등 iterable 자료형 b가 a에 입력되었을 때 참인 경우만 반환한다.
print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6])))

# hex(x) 정수 x를 16진수형태 문자열로 돌려준다.
print(hex(3))

# id(x) 객체x의 주소값을 반환한다.
print(id(3))
print(id(3))

# input(x) 사용자 입력을 받는 함수. x는 생략이 가능하고 입력 시 프롬프트가 된다.
# input('root@')

# int(x) 입력한 문자열 형태의 숫자 또는 소수점이 있는 숫자를 정수형태로 반환한다.
print(int('3'))
# 문자열은 정수만 가능하다. 소수점은 오류가 발생함
# print(int('3.4'))

# int(x, radix)는 radix 진수로 표현된 문자열을 10진수로 반환한다.
print(int('1011', 2))

# isinstance(object, class) object가 class의 인스턴스인지 판단해서 boolean 값을 반환한다.
class Person: pass
p = Person()
print(isinstance(p, Person))

# len(s) 입력값의 길이를 반환한다.
# string
print(len('abcde'))
# tuple
print(len((1, 2, 3)))
# list
print(len([1, 2, 3, 4]))
# set
print(len({1, 2, 3, 4}))
# dict
print(len({'1': 'kat', '2': 'brian'}))

# list(s) 반복 가능한 자료형 s를 입력받아 리스트로 반환한다.
print(list('pypy'))
print(list((1, 2, 3)))

# map(f, iterable) 함수(f)와 반복가능한(iterable) 자료형을 입력받는다. iterable의 요소들을 f에 입력한 결과를 map객체로 반환한다.
print(list(map(lambda x: x * 2, [1, 2, 3, 4])))

# max(iterable) 반복 가늫한자료형을 입력바아 최대값을 반환한다. 숫자는 최대양수, 문자열은 사전순 마지막 문자이다.
print(max([1, 2, 3, 99]))
print(max('python'))

# min(iterable) max와 반대이다
print(min([1, 2, 3, 99]))
print(min('python'))

# oct(x) 정수를 8진수문자열로 반환한다.
print(oct(9))

# open(filename, [mode])

# ord(c) 아스키코드 값을 반환한다.
print(ord('c'))

# pow(x, y) x의 y제곱을 반환한다
print(pow(3, 4))

# range([start], stop, [step]) start[시작숫자], stop[끝숫자], step[증감치]를 의미한다.

# 인수가 1개인 경우는 0부터 시작한다
print(list(range(5)))

# 인수가 2개인 경우는 start부터 stop까지를 의미한다.
print(list(range(5, 10)))

# 인수가 3개인 경우 start부터 stop까지 step만큼 거리가 있는 숫자들을 의미한다.
print(list(range(0, -10, -1)))

# round(number[, ndigits]) ndigits는 생략 가능하다. ndigits는 표시하고싶은 소수점 자릿수이다.
print(round(4.6666))
print(round(4.6666, 2))

# sorted(iterable) 입력값을 정렬해서 결과를 리스트로 반환한다. type으로 검사해도 list로 반환한다.
# sorted와 list의 sort의 차이는 반환값이 다르다. sorted()는 list를 반환하는 반면 list.sort()는 None을 반환한다.
# 기본적으로 오름차순 정렬을 한다.
list1 = list(range(3, -3, -1))
list2 = list(range(3, -3, -1))

print(list1)
print(list2)
print(sorted(list1))
print(list2.sort())
print(list2)

# str(object) 문자열 형태로 객체를 변환해서 반환한다.
print(str(3))
print(str('hi'))
print(str('hi'.upper()))
print(str(list1))

# sum(iterable)은 반복 가능한 자료형을 입력받아 튜플로 바꿔준다.
print(tuple('hi python'))
print(tuple([1, 2, 3]))

# type(object) 자료형이 무엇인지 알려준다
print(type('string'))
print(type(None))
print(type((1,)))

# zip(iterable) 동일한 개수로 이루어진 자료형을 묶는다.
print(list(zip((1, 2, 3), (4, 5, 6))))
print(list(zip((1, 2, 3), (4, 5, 6), (7, 8, 9))))