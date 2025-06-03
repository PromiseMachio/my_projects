#This code will handle the errors incase you don't add a number to be squared.
while True:
    reply = input('Enter Number:')
    if reply == 'stop'and 'exit' and 'quit':
        break
    elif not reply.isdigit():
        print('Bad' *8)
    else:
        print(int(reply) **2)
    
