import threading

data = input("enter string")
def num():
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
t1=threading.Thread(target=let)
t2=threading.Thread(target=num)
t3=threading.Thread(target=sp)

t1.start()
t2.start()
t3.start()