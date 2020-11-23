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

if (money >= 3000) | card:
    print("택시를 타자2")
else:
    print("걸어가~2")

# in, not in
