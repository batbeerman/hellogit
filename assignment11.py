import _thread
import time
import math
import threading

#Q1 Create a threading process such that it sleeps for 5 seconds and then prints out a message.

def printthread(threadn,delay):
    count=0
    while count<10:
        time.sleep(delay)
        count+=1
        print(threadn, time.ctime(time.time()))
try:
    _thread.start_new_thread(printthread("Thread",5))
except:
    print("Thread can't be started")
while 1:
    pass



#Q2 Make a threadthat prints numbers from 1-10, waits for 1 sec between

import _thread
import time
def counter(threadn,delay):
    count=0
    while count<10:
        time.sleep(delay)
        count+=1
        print(count, time.ctime(time.time()))
try:
    _thread.start_new_thread(counter("Thread",10))
except:
    print("Thread ends")
while 1:
    pass



#Q3 Make a list that has 5 elements

def printlis():
    list=(4,6,7,5,4)
    for i in range(len(list)):
        time.sleep(2*i)
        print(list[i],time.ctime(time.time()))
try:
    _thread.start_new_thread(printlis())
except:
    print("Thread ends")
while 1:
    pass



#Q4 all factorial function using thread.

def factorial():

    n = int(input("Enter num: "))
    print("Factorial is: ")
    print(math.factorial(n))
    time.sleep(2)

_thread.start_new_thread(factorial())
