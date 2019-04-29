#-*-encoding:utf-8
import threading
import time

class Test(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self._run_num=num

    def run(self):
        global count,mutex
        threadname=threading.current_thread().getName()
        for x in range(int(self._run_num)):
            mutex.acquire()
            count= count + 1
            mutex.release()
            print(threadname,x,count)
            time.sleep()

if __name__ == '__main__':
    global count,mutex
    threads=[]
    num=5
    count=0
    mutex=threading.Lock()
    for x in range(num):
        threads.append(Test(10))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
