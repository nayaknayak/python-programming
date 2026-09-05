import threading
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

def print_paper():
    print("dowloading start")
    time.sleep(5)
    print("downloading complete")
threading.Thread(target=print_paper).start()
print("Start reading")

