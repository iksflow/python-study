import re

# 그루핑
p = re.compile("(ABC)+")
m = p.search("ABCABCABCABC OK?")
print(m.group(1))

# ()를 통해 그루핑을 하고, 인덱스를 통해 해당 그룹의 문자열만 가져올 수 있다.
p = re.compile(r"(\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park   010-1234-1234")
print(m.group(1))
print(m.group(2))
print(m.group(3))

# 재참초(Backreferences)
p = re.compile(r'(\b\w+)\s+\1')
print(p.findall('in in the the'))

# 그루핑된 문자열에 이름 붙이기
p = re.compile(r"(?P<name>\w+)\s+((\d+)[-]\d+[-]\d+)")
m = p.search("park 010-1234-1234")
print(m.group("name"))

# 이름으로 재참조 하는 예시
p = re.compile(r"(?P<word>\b\w+)\s+(?P=word)")
print(p.search('Paris in the the spring').group())

# 전방탐색(Lookahead Assertions)
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())

# (?=...) 긍정형 전방 탐색 예시. :이 등장하는곳 이전까지를 결과물로 반환한다.
p = re.compile(".+(?=:)")
m = p.search("http://google.com:8080")
print(m.group())

# (?!...) 부정형 전방탐색을 이용해 bat, exe 확장자를 걸러내기
p = re.compile(".*[.](?!bat$|exe$).*$")
m = p.match("abdc.doc")
print(m.group())

# 문자열 바꾸기
# sub를 사용해 일치하는 패턴에 문자열을 임의의 문자열로 치환했다.
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes and black belt'))

# count인수를 추가로 전달하면 변경하는 횟수를 제어할수도 있다.
p = re.compile('(blue|white|red)')
print(p.sub('colour', 'blue socks and red shoes and black belt', count=1))

# subn sub메서드와 다른 점은 반환결과의 형태이다. (변경된 문자열, 변경횟수)의 튜플형태로 반환한다.
p = re.compile('(blue|white|red)')
print(p.subn('colour', 'blue socks and red shoes and black belt'))

# sub 메서드를 사용할 떄 참조 구문 사용하기
p = re.compile(r"(?P<name>\w+)\s+(?P<phone>(\d+)[-]\d+[-]\d+)")
# \g<name> 을 통해 그룹을 참조할 수 있다.

print(p.sub("\g<phone> \g<name>", "park 010-1234-1234"))
print(p.sub("\g<2> \g<1>", "park 010-1234-1234"))

# Greedy 조건을 만족하는 최대의 값을 반환한다. <html>의 '<' 부터 </title>의 '>'까지가 범위이다. </title로 변경하면 그 전인 <title>의 '>'까지가 범위이다.
s = '<html><head><title>Title</title>'
print(len(s))
print(re.match('<.*>', s).span())
print(re.match('<.*>', s).group())

# Non-Greedy 가장 처음 조건을 충족하는 대상만을 반환함. 따라서 <html> 만 매치된다.
print(re.match('<.*?>', s).group())