import random


#Q1
f1=open("File.txt","r+")
n=int(input("Enter position in file: "))
f1.seek(n,0)
print(f.read())
f1.close()



#Q2
f2=open("Woah.txt")
s=f2.read()
d=s.split()
print(d)
n=input("Enter word whose frequency is to be calculated: ")
if n in s:
 print(s.count(n))
f2.close()


#Q3
f3=open("File.txt","r+")
data=f3.read()
f2=open("Woah.txt","w")
f2.write(data)
f3.close()
f2.close()



#Q4
f4=open("copy1.txt","r")
f5=open("copy2.txt","r")
p=f4.readlines()
t=f5.readlines()
for i in range(len(p)):
 for j in range(len(t)):
    if(i==j):
      e=str(p[i])+str(t[j])
      print(e)
f5.close()
f4.close()



#Q5
f6=open("file1.txt","r+")
for i in range(10):
    f6.writelines(str(i))
data=f6.read()
f6.close()
newdata=sorted(data)
file=open("New.txt","r+")
file.write(newdata)
file.close()





