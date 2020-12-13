def add(a, b):
    return a + b

def sub(a, b):
    return a - b

# 파이썬의 내부 변수 __name__
# python ModuleExample.py로 직접 실행 시 __name__ = __main__
# import ModuleExample로 import 시 __name__ = ModuleExample
# 아래 코드는 직접실행 하는경우 print 하겠다는 의미와 같다.
if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 1))