while True:
    num1 = input('Enter num1')
    if num1.lower() == 'exit':
        break
    num2 = input('Enter num2')
    if num2.lower() == 'exit':
        break
    operator = input('Enter operator(+,-,*,/)')
    if operator.lower() == 'exit':
        break
    if not num1.isdigit():
        print('Enter a valid number!')
        continue
    if not num2.isdigit():
        print('Enter a valid number!')
        continue
    num1 = float(num1)
    num2 = float(num2)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print('Error! Division by zero')
        else:
            result = num1 / num2
    print(f"Result:{result}")
        
    
    
