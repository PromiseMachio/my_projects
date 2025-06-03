while True:
    print('Welcome To MY CALC version 3.0')
    print(" Let's do some maths")
    print("If you want to exit type quit----")
    print('Enjoy!!!!!!!!!')
    #User inputs
    num1 = input('Enter First Number:')
    if  num1.lower() ==  'quit':
        break
    num2 = input('Enter Second Number:')
    if num2.lower() ==  'quit':
        break
    operator = input('Enter Operator( +, -, *, /):')
    if operator.lower() == 'quit':
        break
    #Validating if the inputs are valid
    if not (num1.replace('.','',1).isdigit() and num2.replace('.','',1).isdigit()):
        print('Invalid input')
        continue
    #Machine checking data inputs storages
    num1 = float(num1)
    num2 = float(num2)

    #Mathematical operations.
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print('Number cannot be divided by 0')
            continue
        result = num1 / num2
    else:
        print('Invalid operator')
        continue
    print(f"Result:{result}")
    
    
    
    
    
