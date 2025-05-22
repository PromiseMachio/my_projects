guess = 30
while True:
    guess = int(input('Guess a number between 1 to 100'))
    if guess == 30:
        print('Correct')
        break
    elif guess < 30:
        print('Too low')
        continue
    elif guess > 30:
        print('Too high')
        continue
