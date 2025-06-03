#The code will incluide if in the elif statement in the third excecution expression.
while True:
    reply = input('Enter Number:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' *3)
    else:
        num = int(reply)
        if num < 20:
            print('Too low')
        else:
            print(num **2)
print('Bye!')
