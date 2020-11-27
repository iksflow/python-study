# for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)] # , (7,) 가 들어가면 오류남
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

# range를 통해 리스트를 만들기
range_test = range(4, 10)
print("range_test = ", range_test)
for i in range_test:
    print(i)

# 1부터 10까지 더하기
range_ten = range(1, 11)
sum = 0
for i in range_ten:
    sum += i
print("sum = ", sum)

# 리스트 내포(List comprehension) 사용하기
list_test = [1, 2, 3, 4]
result = [num * 3 for num in list_test]
for i in result:
    print(i)

# 리스트 내포 기법을 이용해 구구단 만들기
nine_by_nine = [x * y for x in range(2, 10) for y in range(1, 10)]
for i in nine_by_nine:
    print("i = ", i)