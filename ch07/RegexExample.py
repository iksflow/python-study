import re

# p(패턴)는 정규식을 컴파일 한 결과를 의미한다.
p = re.compile('[a-z]+')

# 패턴과 문자열이 일치하는 경우 match 객체를 반환
m = p.match("python")
print(m)

# 패턴과 문자열이 일치하지 않는 경우 None을 반환
m = p.match("3 python")
print(m)

# 일반적인 정규표현식 활용 흐름
if m:
    print("match found:", m.group())
else:
    print("no match")

# search는 전체를 검색한다. 따라서, python을 찾아낸다.
m = p.search("3 python")
print(m)

# findall 패턴과 일치하는 모든 문자열을 반환한다.
result = p.findall("life is too short")
print(result)

# finditer 패턴과 일치하는 반복가능한 객체를 돌려준다. 반복객체의 요소들은 match객체이다.
result = p.finditer("life is too short")
print(result)
for r in result: print(r)

# match객체의 메서드

m = p.search("python")
# group() 매치된 문자열을 반환한다.
print("m.group()", m.group())

# start() 매치된 문자열의 시작 위치를 반환한다.
m = p.search("3 python")
print("m.start()", m.start())
# end() 매치된 문자열의 끝 위치를 반환한다.
m = p.search("3 python")
print("m.end()", m.end())
# span() 매치된 문자열의 (시작, 끝)에 해당하는 튜플을 반환한다.
m = p.search("3 python")
print("m.span()", m.span())

# 1회성 패턴의 경우 re.match("표현식", "조사문자열") 형태로 사용하는것이 더 간편하다.
m = re.match("[a-z]+", "python")
print(m.group())

# 컴파일 옵션

# DOTALL(or S) dot(.)문자가 줄바꿈을 포함 해 모든 문자와 매치가 되도록 한다.

# .은 모든문자를 대상으로 하지만 줄바꿈문자('\n') 만은 예외로 검색하지 않는다. 따라서 None을 반환하게 된다.
p = re.compile("a.b")
m = p.match("a\nb")
print(m)

# 옵션으로 DOTALL을 주게되면 빈문자열도 검색대상에 포함하게된다.
p = re.compile("a.b", re.DOTALL)
m = p.match("a\nb")
print(m)