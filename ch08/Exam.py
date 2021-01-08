# Q1. 문자열 바꾸기
# a:b:c:d -> a#b#c#d
q1 = 'a:b:c:d'
print(q1.replace(':', '#'))

# Q2. 딕셔너리 값 추출하기. - 존재하지 않는 C라는 키를 호출했을 때, 오류 대신 70이 출력되게하기
a = {'A':90, 'B':80}
# print(a['C'])

# Q3. 리스트의 더하기와 extend 함수 - +, extend의 결과물 차이를 설명
# 더하기는 새로운 리스트 객체를 생성, extend는 기존 객체를 변경
a = [1, 2, 3]

b = a + [4, 5]
a.extend([4, 5])

# Q4. 리스트 총합 구하기 - 50점 이상 점수의 총합 구하기
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = sum(filter(lambda x: x >= 50, A))
print(result)

# Q5. 피보나치 함수 - 정수 n을 입력받았을 때, n 이하의 피보나치수열을 출력하는 함수를 작성하기
# 0, 1, 1, 2, 3, 5, 8, 13
def fibonaci(n):
    list = [0, 1]

    next = 0
    while next <= n:
        next = list[len(list) - 1] + list[len(list) - 2]
        if next <= n:
            list.append(next)
        else:
            pass
    return list
print(fibonaci(5))
# Q6. 숫자의 총합 구하기 - 입력받은 숫자의 총합을 구하는 프로그램을 작성
# 65,45,2,3,45,8
listStr = '65,45,2,3,45,8'
list = listStr.split(',')
sum1 = 0
for i in range(len(list)):
    sum1 += int(list[i])
print('sum1 =', sum1)

# Q7. 한 줄 구구단 - 2~9의 숫자 중 하나를 입력받아 구구단 출력하기
def gugu(n):
    for i in range(1, 10):
        print(n * i, end = ' ')
gugu(2)

# Q8. 역순 저장
f = open('C:/Users/iksflow/PycharmProjects/python-study/ch08/abc.txt', 'r')
data = f.readlines()
data.reverse()
print('\ndata\n', data)
f.close()
f = open('C:/Users/iksflow/PycharmProjects/python-study/ch08/abc.txt', 'w')
for i in range(len(data)):
    f.write(data[i].replace('\n', '')+'\n')
f.close()

# Q9. 평균값 구하기 - sample.txt의 숫자 값을 모두 읽어 총합과 평균을 구한 후 평균값을 result.txt파일에 쓰는 프로그램 작성하기
f = open('C:/Users/iksflow/PycharmProjects/python-study/ch08/sample.txt', 'w')
data = """70
60
65
75
95
90
80
80
85
100"""
f.write(data)
f.close()

f = open('C:/Users/iksflow/PycharmProjects/python-study/ch08/sample.txt', 'r')
sum1 = 0
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print('readline=', f.readline())
# print(f.__next__())
# while f.readable():
#     print('readline=', f.readline())
    # sum += int(f.readline())
print(sum1)
f.close()

# Q10. 사칙연산 계산기
class Calculator:
    def __init__(self, elements):
        self.elements = elements
    def sum(self):
        return sum(self.elements)
    def avg(self):
        return sum(self.elements) / len(self.elements)

cal = Calculator([1, 2, 3, 4, 5])

print(cal.elements)
print(cal.sum())
print(cal.avg())

# Q11. 모듈 사용방법

# Q12. 오류와 예외 처리
print("Q12")
result12 = 0
try:
    [1, 2, 3][3]
    "a"+1
    4 / 0
except TypeError:
    result12 += 1
except ZeroDivisionError:
    result12 += 2
except IndexError:
    result12 += 3
finally:
    result12 += 4
print(result12)

# Q13. DashInsert 함수
def DashInsert(str):
    result = ''
    for i in range(len(str)):
        if i == 0:
            result += str[i]
            continue
        if (int(result[-1]) & 1) == (int(str[i]) & 1):
            if (int(str[i]) & 1 == 0):
                result += '*' + str[i]
            else:
                result += '-' + str[i]
        else:
            result += str[i]
    return result

str13 = '4546793'
print(DashInsert(str13))

# Q14. 문자열 압축하기 문자열을 입력받아 같은 문자가 반복되는 경우 반복횟수를 표시해 압축하라
def ZipFunction(text):
    result = ''
    last = ''
    count = 1
    for i in range(len(text)):
        if (i == 0):
            last = text[i]
            continue
        if (last == text[i]):
            count += 1
        else:
            result += last + str(count)
            last = text[i]
            count = 1
        if (i == len(text) - 1):
            result += last + str(count)

    return result
str14 = 'aaabbcccccca'
print(ZipFunction(str14))

# Q15. Duplicate Numbers - 0~9의 숫자로 이루어진 문자를 입력받았을 때, 중복된 숫자가 존재하는지 확인하는 함수를 작성하시오
def checkDup(str):
    checker = [False] * 10
    for i in range(len(str)):
        if checker[int(str[i])] == True:
            return False
        else:
            checker[int(str[i])] = True

    return True

print(checkDup('0123456789'))

# Q16. 모스 부호 해독 - 문자열 형식으로 입력받은 모스 부호를 해독하여 영어 문장으로 출력하는 프로그램을 작성하라
morseMap = {
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..':'L',
    '--':'M',
    '-.':'N',
    '---':'O',
    '.--.':'P',
    '--.-':'Q',
    '.-.':'R',
    '...':'S',
    '-':'T',
    '..-':'U',
    '...-':'V',
    '.--':'W',
    '-..-':'X',
    '-.--':'Y',
    '--..':'Z',
}
def morseInterpreter(str):
    codes = str.split(' ')
    result = ''
    for i in range(len(codes)):
        result += morseMap.get(codes[i])
    return result
str = '.... . ... .-.. . . .--. ... . .- .-. .-.. -.--'
print(morseInterpreter(str))
