import time
import calendar
import webbrowser

# UTC 시간
print(time.time())

# time.localtime
print(time.localtime())

# time.asctime
print(time.asctime(time.localtime(time.time())))
print(time.asctime())

# time.ctime 현재시간돌려줌
print(time.ctime())

# time.strftime 포맷에 맞게 시간을 표현한다

print(time.strftime('%Y%m%d', time.localtime()))

time.sleep(1)
for i in range(10):
    print(i)
    time.sleep(1)

print(calendar.calendar(2015))

webbrowser.open("www.naver.com")