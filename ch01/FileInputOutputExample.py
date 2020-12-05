# 파일 입출력

# 파일을 생성한다. 쓰기모드
f = open("C:/doit/새파일.txt", "w")

# 파일에 내용 쓰기
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)

# close를 사용해 파일을 닫아줘야한다. 닫지않은 파일은 다시 사용하려고 하는경우 오류가 발생함.
f.close()

# 파일을 읽기모드로 열기
f = open("C:/doit/새파일.txt", "r")
line = f.readline()
# 한줄 읽기
print(line)

# 여러줄 읽기
lines = f.readlines()
for i in lines:
    print(i)
f.close()