#import threading
import time

"""
def task_one():
    print("threading one start")
    time.sleep(5)
    print("task one complete")
    
def task_two():
    print("threading two start")
    time.sleep(4)
    print('threading two complete')
    
threading.Thread(target=task_one).start()
threading.Thread(target=task_two).start()
"""
a=50;
def print_paper():
    print("dowloading start")
    print(a)
    b= 20
    time.sleep(5)
    print("downloading complete")
    print(b)
print_paper()
"""
ts=threading.Thread(target=print_paper)
ts.start()
ts.join()
print("Start reading")

"""