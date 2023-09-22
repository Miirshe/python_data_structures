def sentence_convert_tuples(sentence):
    try:
        data_list = sentence.split(' ')
        data_tuple = tuple(data_list)
        for i in data_tuple:
            print(i)
        first_name , second_name , last_name , age , *others = data_tuple
        print(f'First_name : {first_name}\nSecond_name : {second_name}\nLast_name : {last_name}\nAge : {age}\nothers : {others}')
    except IndexError:
        print('Index Out Of Range ')
    else:
        print('Enjoy🙋‍😇😇')
    finally:
        print('finally keyword every time executes')
sentence_convert_tuples('abdikafi isse Isak  20 ')

# swapping two variable by using unpacking
x = 20
y = 30
x , y = y , x
print(f'x : {x} y : {y}')
