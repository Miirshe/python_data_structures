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


def list_fruits():
    try:
        fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
        index_fruits = [index for index in fruits]
        for i in index_fruits:
            print(f'{index_fruits.index(i)} : {i}')
    except IndexError:
        print('Index Out Of Range ')
    else:
        print('Enjoy🙋‍😇😇')
    finally:
        print('finally keyword every time executes')


list_fruits()
