import threading
import os

def square(num):
    print("square=",num*num)
def cube(num):
    print ("cube=",num*num*num)

def details():
    print(os.getpid())
    print(threading.current_thread().name)

data = input("enter string")
def nums():
    result=""
    for ch in data:
        if ch.isdigit():
            result+=ch
    print (result)


def let():
    result=""
    for ch in data:
        if ch.isalpha():
            result+=ch
    print (result)

def sp():
    result=""
    for ch in data:
        if not ch.isalnum() and not ch.isspace():
            result+=ch
    print (result)    

num = int(input("enter a num"))
t1=threading.Thread(target=square,args=(num,))    
t2=threading.Thread(target=cube,args=(num,)) 

t3=threading.Thread(target=details,name="thread1") 

t4=threading.Thread(target=let)
t5=threading.Thread(target=nums)
t6=threading.Thread(target=sp)

t1.start()
t2.start()
t3.start()
t5.start()
t4.start()
t6.start()

