import random

text_1 = 'Enter the number of friends joining (including you):\n'
text_2 = 'Enter the name of every friend (including you), each on a new line:'
text_3 = 'Enter the total bill value:\n'
text_4 = 'Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'

def check_number_friends(number_friends):
    if number_friends <= 0:
        print('No one is joining for the party\n')
        exit()


def divide_bill(total_bill, number_friends):
    return round(total_bill/number_friends, 2)


def enter_number():
    number_friends = int(input(text_1))
    check_number_friends(number_friends)
    return number_friends


def insert_friends(number_friends):
    print(text_2)
    return {input(): 0 for _ in range(number_friends)}


def insert_bill(dictionary, number_friends):
    total_bill = int(input(text_3))
    p = divide_bill(total_bill, number_friends)

    for item in dictionary.keys():
        dictionary[item] = p
    print(dictionary)
    return total_bill

def lucky_feature(dictionary, total_bill):
    option = input(text_4)
    if option == 'Yes':
        lucky = random.choice(list(dictionary.keys()))
        print(f'{lucky} is the lucky one!')

        new_p = round(total_bill / (len(dictionary.keys()) - 1), 2)
        for obj in dictionary.keys():
            dictionary[obj] = new_p
        dictionary[lucky] = 0
    else:
        print('No one is going to be lucky')
    print(dictionary)

def menu_display():
    number_friends = enter_number()
    dictionary = insert_friends(number_friends)
    total_bill= insert_bill(dictionary, number_friends)
    lucky_feature(dictionary, total_bill)


if __name__ == '__main__':
    menu_display()
