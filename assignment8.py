import os
import math
import time
import datetime
from datetime import date

#Q1 time tuple
# Python stores time in tuples, there are a total of nine tuples.
#Index	Field	        Domain of Values

#0	Year(4 digits)	Ex.- 1995
#1	Month	        1 to 12
#2	Day	        1 to 31
#3	Hour	        0 to 23
#4	Minute	        0 to 59
#5	Second	        0 to 61 (60/61 are leap seconds)
#6	Day of Week	0 to 6 (Monday to Sunday)
#7	Day of Year	1 to 366 (Julian day)
#8	DST	        -1,0,1



#Q2  Write a program to get formatted time.
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)


#Q3 Extract month from the time.
now = datetime.datetime.now()
print( now.month)


#Q4  Extract day from the time.
now = datetime.datetime.now()
print( now.day)


#Q5 Extract date (ex : 11 in 11/01/2021) from the time.
t = datetime.datetime.now()
print(t)
print(t.day)



#Q6 Write a program to print time using localtime method.
localtime = time.localtime(time.time())
print("Local current time :", localtime)


#Q7 Find the factorial of a number input by user using math package functions.
num=int(input("Enter the number"))
print("The factorial of number is", math.factorial(num))


#Q8 Find the GCD of a number input by user using math package functions.
m=int(input("Enter a number"))
n=int(input("Enter a number"))
print("GCD of two number is",math.gcd(n,m))


#Q9  Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.
print(os.getcwd())
print(os.environ)
