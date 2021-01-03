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
sum = 0
for i in range(len(list)):
    sum += int(list[i])
print('sum =', sum)

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
sum = 0
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
print(sum)
f.close()