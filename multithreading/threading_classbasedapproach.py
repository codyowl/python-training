import threading
import time

class Threadingclass(threading.Thread):
    def __init__(self, time):
        super(Threadingclass, self).__init__()
        self.time = time
        self.start()

    def run(self):
        print self.time, " seconds start!"
        for i in range(0,self.time):
            time.sleep(1)
            print "1 sec of ", self.time
        print self.time, " seconds finished!"


t1 = Threadingclass(3)
t2 = Threadingclass(2)
t3 = Threadingclass(1)
t1.join()
print "t1.join() finished"
t2.join()
print "t2.join() finished"
t3.join()
print "t3.join() finished"