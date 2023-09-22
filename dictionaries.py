# def count_letter(sentence):
#     letters = [letter for letter in sentence]
#     char_fruency = {};
#     for letter in letters:
#         if letter in char_fruency:
#             char_fruency[letter] += 1;
#         else:
#             char_fruency[letter] = 1;
#     char_freuency_sorted = sorted(char_fruency.items(),key= lambda kv : kv[1] , reverse=True)
#     print(char_freuency_sorted)
# count_letter('this is a common interview question')

#split words and store dictionary and read all characters
def split_word(sentence):
    letters = [letter for letter in sentence]
    my_dictionary = {}
    for letter in letters:
        if letter in my_dictionary :
            my_dictionary[letter] += 1;
        else:
            my_dictionary[letter] = 1
    print(sorted(my_dictionary.items()))
split_word('hi miirshe how fell your day ')

# created dictionary add some key and pair values
def create_dictionary():
    my_dict = {
        'username':'miirshe',
        'email':'miirshe@gmail.com',
        'password':'12345'
    }
    #key() method return all key in dictionary
    # for key in my_dict.keys():
    #     print(key)
    # print(my_dict.keys())

    # values() method return all values in dictionary
    # for value in my_dict.values():
    #     print(value)
    # print(my_dict.values())

    # access  values of dictionary by using get() method
    # if 'username' in my_dict.keys():
    #     print(my_dict.get('username'))
    # else:
    #     print('Not Found This Key !')

    # update() method provides you update keys by values
    # if 'username' in my_dict.keys():
    #     my_dict.update({'username':'miirshe'})
    #     print(my_dict)
    #     print('successfully Updated')

    # update() method provides you update keys
    for key in my_dict.keys():
        if 'username' == key :
            key = 'name'
            my_dict['username']=key;
            print(my_dict)
create_dictionary()



