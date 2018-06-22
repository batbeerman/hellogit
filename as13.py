#Q1
#Zero division error
a=3
try:
 if a<4:
   a=a/(a-3)
   print(a)
except ZeroDivisionError:
 print("Error!")


#Q2
#Out of index error
l=[1,2,3]
try:
 print(l[3])
except IndexError:
 print("Error!")


#Q3
#Output
#An exception will be raised
'''
An exception
Traceback (most recent call last):
  File "C:/Users/Shivangi/PycharmProjects/Project1/trial.py", line 4, in <module>
    raise NameError("Hi there")  
NameError: Hi there
'''


#Q4
'''
-5.0
a/b result in 0
'''



#Q5
try:
 import Error
except ImportError:
 print("No error imported")

try:
 l=[1,2,3]
 print(l[3])
except IndexError:
 print("Out of Index")

try:
   s=int(input("Enter Number"))
   print(s)
except ValueError:
 print("Value Error")



#Q6
class AgeTooSmallError(Exception):
   pass
while(1):
 s =int(input("Enter age"))
 try:
  if s < 18:
   raise AgeTooSmallError
  else:
   print("Valid ")
   break
 except AgeTooSmallError:
   print("Invalid ")
