while True:
    try:
        print('This is an adding machine')
        first_number = int(input('What is the first number you want to add?'))
        second_number = int(input('What is the second number you want to add'))
        sum = first_number + second_number
        print('The sum of your two numbers is', sum)
        break
    except:
        print('Your input is not correct...')