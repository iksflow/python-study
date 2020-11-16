# 딕셔너리 정의하기

# key:value의 구조로 정의한다.
dic = {"name":"iksflow", "phone":"01012345678", "birth":"20201116"}
print("dic : ", dic)

# key를 이용해 value 얻기
print("dic['name'] = ", dic["name"])

# 중복된 key로 value 할당하는 경우, 마지막에 정의된것이 나옴.
dic2 = {1:"a", 1:"b"}
print("dic2 : ", dic2)

# key에 리스트를 입력하는 경우, 오류 발생. key는 불변값만 사용할 수 있음
# dic3 = {[1]:'a'}
# print("dic3 : ", dic3)

# key에 튜플을 입력하는 경우, 정상 동작. 튜플은 불변값이기 때문에 리스트와 다르게 사용 가능.
dic4 = {(1,2):'a'}
print("dic4 : ", dic4)

# 딕셔너리 관련 함수들

