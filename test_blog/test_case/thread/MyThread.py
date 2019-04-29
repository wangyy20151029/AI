#coding:utf-8
import threading

class MyThread(threading.Thread):

    def __init__(self,name=None):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        print(self.name)

    def test():
        for i in range(0,100):
            t=MyThread("thread_" + str(i))
            t.start()

if __name__ == '__main__':
    MyThread.test()