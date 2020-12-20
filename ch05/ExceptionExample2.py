from MyError import MyError
def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick('천사')
    say_nick('바보')
except MyError as e:
    # 사용자 정의 예외클래스를 사용하는 경우 __str__메서드를 구현해야한다.
    print(e)