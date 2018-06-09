x = int(input('Enter age of x : '))
y = int(input('Enter age of y : '))
z = int(input('Enter age of z : '))
if(x>y):
    if(x>z):
        print('X is eldest')
    else:
        print('Z is eldest')
        
if(y>x):
    if(y>z):
        print('Y is eldest')
    else:
        print('Z is eldest')

if(x<y):
    if(x<z):
        print('X is youngest')
    else:
        print('Z is youngest')

if(y<x):
    if(y<z):
        print('Y is youngest')
    else:
        print('Z is youngest')
        
