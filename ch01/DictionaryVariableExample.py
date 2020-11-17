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
dic5 = {'name': 'iksflow', 'phone': '01012345678', 'birth': '1117'}
print('dic5 : ', dic5)

# keys() 함수는 dict_keys객체를 반환한다.
print('dic5.keys() = ', dic5.keys())

for key in dic5.keys():
    print('key = ', key)

# dict_keys객체를 리스트로 변환
print('list(dic5.keys()) = ', list(dic5.keys()))

# values()를 사용해 dict_values 객체 얻기
print('dic5.values() = ', dic5.values())

# items()를 사용해 dict_items 객체 얻기
print('dic5.items() = ', dic5.items())

# 딕셔너리 모두 지우기
dic6 = {'name': 'iksflow', 'phone': '01012345678', 'birth': '1117'}
dic6.clear()
print('dic6 = ', dic6)

# get함수로 value 얻기
dic7 = {'name': 'iksflow', 'phone': '01012345678', 'birth': '1117'}
print('dic7.get("name") = ', dic7.get("name"))

# 특정 key가 포함되어있는지 확인하기
print('"name" in dic7 : ', 'name' in dic7)


