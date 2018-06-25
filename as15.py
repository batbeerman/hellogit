import re

#Q1
email="zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
s=re.findall(r'([a-z]+\d+)@([a-z]+).([a-z]+m)',email)
print(s)


#Q2
find = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
res=re.findall(r'[bB]\w+',find)
print(res)



#Q3
find1=",;_"
input = "A, very very; irregular_sentence"
for i in find1:
 input=input.replace(i,' ')
 input.split()
print(input)
