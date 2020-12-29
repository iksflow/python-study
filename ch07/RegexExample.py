import re

# p(패턴)는 정규식을 컴파일 한 결과를 의미한다.
p = re.compile('ab*')

# 패턴과 문자열이 일치하는지 확인한다
p.match()