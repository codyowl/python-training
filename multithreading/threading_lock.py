import threading
import time
import inspect

#inspect module:
#The inspect module provides several useful functions to help 
#get information about live objects such as modules, classes, 
#methods, functions, tracebacks, frame objects, and code objects

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

count = 0
lock = threading.Lock()

def incre():
    global count
    caller = inspect.getouterframes(inspect.currentframe())[1][3]
    print "Inside %s()" % caller
    print "Acquiring lock"
    with lock:
        print "Lock Acquired"
        count += 1  
        time.sleep(2)  

def bye():
    while count < 5:
        incre()

def hello_there():
    while count < 5:
        incre()

def main():    
    hello = Thread(hello_there)
    goodbye = Thread(bye)


if __name__ == '__main__':
    main()