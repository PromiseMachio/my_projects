#In this code we are going to  write a program with try and exception statements that's if the the Try part fails it runs the exception part.
while True:
    reply = input('Enter Number')
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
        print('Bad!')
    else:
        print(int(reply))
print('Bye!')
print('---------------------------')
#try statement case 2:
while True:
    try:
        num = int(input('Enter number (or q to quit):'))
        print(f"You have entered: {num}")
        print("The division by 2:", num // 2)
        print(f"The factor of {num}:", num **2)
    except ValueError:
        user_input = input('Invalid Input. Do you want to quit (y/n):').lower()
        if user_input == 'y' or user_input == 'q':
            print('Exiting loop!')
            break
        else:
            print("Let's try again!")
        print(num **2)

print('--------------------------------')
