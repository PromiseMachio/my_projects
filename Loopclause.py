y = int(input('Enter a number:'))
x = y // 2
while True:
    if y % x == 0:
        print(y, 'has factor', x)
        break
    else:
        if  not y.isdigit():
            print('Enter a valid number')
    x -= 1
else:
    print(y, 'Is a prime number')

print('-------------------------------')














    
