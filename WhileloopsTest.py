#The codes below intesively checks and explain all about while loops statements.
while True:
    print('Machio you are amaizing manh')
    break
print('----------------------------------')
x = 'Spam'
while x:
    print(x, end =' ')
    x = x[1:]

print('-----------------------')
#This code counts numbers from a to b but not including b using while loop.
a =0 ; b = 10
while a < b: #one way code counter loops
    print(a, end=' ')
    a+= 1

print('--------------------------------------')

print('---------------------------------------')
i = 10
while True:
    if i % 7 == 0:
        break
    i += 1
    
            
