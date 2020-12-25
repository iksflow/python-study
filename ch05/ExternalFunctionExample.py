import pickle
import os
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

f2 = open("test.txt", 'rb')
data2 = pickle.load(f2)
print(data2)
f2.close()

print(os.environ['PATH'])
oridir = os.getcwd()
os.chdir("C:\WINDOWS")
print(os.getcwd())
os.chdir(oridir)
# 시스템에서 dir명령어를 실행한 값을 돌려받는다.
print(os.system("dir"))
f3 = os.popen("dir")
print(f3.read())