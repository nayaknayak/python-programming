"""


def greet():
    print("welcome to pythons")
greet()


def greet(name,courses="Gen Ai"):
    print(f"hi {name}, i am doing {courses} courses here ")
greet("Satya","java")


def number_count(*args):
    print(args)
number_count(10,20,30)

msg = "hi i am learning java"

def print_msg():
    global msg
    msg= "i am learning python"

print_msg()
print(msg)
"""

def greet(name):
    print(' Good morning ', name )