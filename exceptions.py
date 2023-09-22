def leap_year():
    try:
        year = int(input('Enter Year ? : '))
        if year % 4 == 0 and year % 400 == 0 :
            print(f'{year} is a leap year ! ')
        else:
            print(f'{year} is not a leap year')
    except (ValueError, ZeroDivisionError,):
        if ValueError :
            print(f'Enter Integer Number. not allowed string type')
        if ZeroDivisionError :
            print(f'Zero is not numerato')
leap_year()
