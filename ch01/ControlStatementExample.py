# if문 : 들여쓰기를 통해서 특정 조건인 경우 수행할 문장을 구분하므로 반드시 지켜야한다.

money = True
if money:
    print("택시를 타고 간다")
# print("hehe")  들여쓰기로 인해 오류 발생
else:
    print("걸어 간다")
    
    
# 기본 비교연산자 =, !=, >, < 등은 다른 언어와 같으니 생략

# and(&), or(|), not(!)
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타자")
else:
    print("걸어가~")
# elif 를 통해 추가 조건을 정의할 수 있다.
if money >= 3000:
    print("택시를 타자2")
elif card:
    print("카드가 있으니 타자")
else:
    print("걸어가~2")

# 조건부 표현식을 사용해 조건문을 한줄로 표현하기
score = 60
mesage = "success" if score >= 60 else "failure"
print("message = ", mesage)
# in, not in
list = [1, 2, 3]
print("1 in list = ", 1 in list)
tuple = (1, 2, 3)
print("4 in tuple = ", 4 in tuple)
print("4 not in tuple = ", 4 not in tuple)

# 반복문

# while
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10:
        print("나무 넘어갑니다")

prompt = """
    1. Add
    2. Del
    3. List
    4. Quit
    
    Enter number: """
number = 0
while number != 4:
    print(prompt)
    number = int(input())

coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
# for

# for 1 in [1, 2, 3, 4]
