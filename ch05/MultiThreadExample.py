import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")
threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()
    # start와 동시에 join을 하면 현재 루프에서의 t가 끝날떄까지 기다리게되므로 multithread의 이점을 살리지 못하게됨.
    # t.join()
for t in threads:
    t.join()

print("End")