#Q.1- Create a list with user defined inputs.

list = []
for i in range(10):
    x = int(input("Enter element \n"))
    list.append(x)
    i += 1
print('List : \n')
for i in range(len(list)):
    print(list[i])



#Q.2- Add the following list to above created list: [‘google’,’apple’,’facebook’,’microsoft’,’tesla’]

while(True):
    print("PUBG")



#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.

test_list = []
n=int(input("Enter range"))
for i in range(n):
    x = int(input("Enter the element \n"))
    test_list.append(x)
for i in range(len(test_list)):
    test_list[i] = test_list[i] * test_list[i]
for i in range(len(test_lis)):
    print(test_list[i])



#From a list containing ints, strings and floats, make three lists to store them separately 

lis= []
n=int(input("Enter total number of elements"))
for i in range(n):
    x = int(input("Enter the element \n"))
    lis.append(x)
for i in range(len(lis)):
    lis[i]=lis[i]*lis[i]
for i in range(len(lis)):
    print(lis[i])




#Q.5- Using range(1,101), make a list containing even and odd numbers.

odd = []
even = []
for x in range(1,101):
    if x%2 == 0:
        odd.append(x)
    else:
        even.append(x)
print('ODD list',odd)
print('EVEN list',even)


#Q.6- Print the following patterns: 

for i in range(0,4):
    for j in range(0,i+1):
        print("*", end=" ")
    print('\n')


#Q.7- Create a user defined dictionary and get keys corresponding to the value using for loop.

my_dict = dict()
n=int(input("Enter number of elements"))
for i in range(n):
 key = input("Enter the key: ")
 value = input("Enter the value: ")
 my_dict[key] = value
for k in my_dict:
    print(my_dict[k])


#Q.8- Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop

dell = []
n = int(input("Enter total number of elements"))
for i in range(n):
    x = input("Enter the element \t")
    dell.append(x)
o = int(input("Enter element to be deleted"))
for i in range(len(dell)):
    if dell[i] == o:
        del dell[i]
for i in range(len(dell)):
    print(dell[i])
