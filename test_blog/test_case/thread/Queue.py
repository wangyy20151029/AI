#!/usr/bin/env python
import queue
import threading
import urllib3
import time

hosts=["htts://www.qq.com","https://www.baidu.com","https://www.163.con"]
queue=queue.Queue()

class ThreadUrl(threading.Thread):

    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue=queue

    def run(self):
        while True:
            host=self.queue.get()
            url=urllib3.urlopen(host)
            uri=urllib3.urlopen(host)
            self.queue.task_done()
            start=time.time()

    def main():
        for i in range(5):
            t = ThreadUrl(queue)
            t.setDaemon(True)
            t.start()
            for host in hosts:
                queue.put(host)
                queue.join()
    main()
    print("Elapsed Time: %s" %(time.time() - start))
