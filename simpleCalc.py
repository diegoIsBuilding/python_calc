#Take two numbers and save them to a variable
try:
    # First number 
    num_one = int(input('Please enter the first number: '))

    # Operator (+-*/)
    operator = input('Enter operator: ')

    # Second Number
    num_two = int(input('Please enter the second number: '))

    # List of valid operators
    valid_operators = ['+', '-', '*', '/']

    if operator in valid_operators:
        if operator == '+':
            print(num_one + num_two)
        elif operator == '-':
            print(num_one - num_two)
        elif operator == '*':
            print(num_one * num_two)
        elif operator == '/':
            if num_two == 0:
                print('Cannot divide by zero')
            else:
                print(num_one / num_two)
        else:
            print('Select one of the following operators +, -, *, /')
    else:
        print('Invalid operator. Please select one of the following operators +, -, *, /')

except ValueError:
    print('Invalid input: Enter a number')
