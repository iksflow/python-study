# 오류 예외 처리 기법

# 1. try, except만 쓰는 방법 - 오류 종류에 상관없이 오류가 발생하면 except블록을 수행한다.

try:
    list = [1, 2, 3]
    print(list[3])
except:
    print("오류났지롱~")

# 2. try, except 발생오류 - 특정 오류에 대해서만 except블록을 수행한다.

try:
    list2 = [1, 2, 3]
    print(list2[3])
    print("오류가 발생한 지점 이후의 코드는 실행이 안됩니다")
except IndexError:
    print("IndexError가 발생했다.")

# 3. try, except 발생오류 as 변수 - 발생한 오류와 오류메시지 변수를 포함한 except문

try:
    print(4 / 0)
except ZeroDivisionError as e:
    print("e =", e)
    
# 4. try... finally - finally는 오류가 발생해도 반드시 수행되는 블록이다.
try:
    print(4 / 0)
except ZeroDivisionError:
    print("ZeroDivisionError 발생")
finally: 
    print("Finally블록 수행")