import time
import threading

def squarer(range_number):
    print "executing first function"
    for i in range_number:
        time.sleep(0.2)
        print "first function executed"
        print i * i

def cuber(range_number):
    print "executing second function"
    for i in range_number:
        time.sleep(0.2)
        print "second function executed:"
        print i * i * i         

sequence_list = [12,13,14,15,16,17,18]

kickstarted_time = time.time()

#function execution with threading
first_thread = threading.Thread(target=squarer, args=(sequence_list,))
second_thread = threading.Thread(target=cuber, args=(sequence_list,))

#threading start
first_thread.start()
second_thread.start()

#joing method
first_thread.join()
second_thread.join()

print "Time taken :", time.time() - kickstarted_time