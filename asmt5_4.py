points = int(input('Enter points scored : '))

if((points >=1) & (points <=50)):
    print('Congratulations! You won No prize')
elif((points >=51) & (points <=150)):
    print('Congratulations! You won a Wooden Dog')
elif((points >=151) & (points <=180)):
    print('Congratulations! You won a Book')
elif((points >=181) & (points <=200)):
    print('Congratulations! You won Chocolates')
else:
    print('Invalid points entered')

        
