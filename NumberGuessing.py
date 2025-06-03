while True:
    reply = input('Enter a number:')
    if not reply.isdigit():
        print('Invalid number')
        continue
    reply = int(reply)
    if reply == 30:
        print('correct guessing')
        break
    elif reply < 30:
        print('Too low')
    elif reply > 30:
        print('Too high')
        
    
