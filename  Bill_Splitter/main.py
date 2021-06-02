# Stage 1/4: Invite your friends
# print('Enter the number of friends joining (including you):')
# count_friends = int(input())
# print('')
# dict_friends = {}
# if count_friends > 0:
#     print('Enter the name of every friend (including you), each on a new line:')
#     for i in range(count_friends):
#         dict_friends[input()] = 0
#     print('')
#     print(dict_friends)
# else:
#     print('No one is joining for the party')

# Stage 2/4: The bill has arrived

# print('Enter the number of friends joining (including you):')
# count_friends = int(input())
# print('')
# dict_friends = {}
# if count_friends > 0:
#     print('Enter the name of every friend (including you), each on a new line:')
#     for i in range(count_friends):
#         dict_friends[input()] = 0
#     print('\nEnter the total bill value:')
#     sum_bill = round(int(input()) / count_friends, 2)
#     for k, v in dict_friends.items():
#         dict_friends[k] = sum_bill
#     print(dict_friends)
# else:
#     print('No one is joining for the party')

# Stage 3/4: The Lucky One
import random
print('Enter the number of friends joining (including you):')
count_friends = int(input())
print('')
dict_friends = {}
if count_friends > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count_friends):
        dict_friends[input()] = 0

    print('\nEnter the total bill value:')
    sum_bill = round(int(input()) / count_friends, 2)

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    result = input().lower()
    if result == 'yes':
        random_friend = random.choice(list(dict_friends.keys()))
        print(f'{random_friend} is the lucky one!')
    else:
        print('No one is going to be lucky')
    # for k, v in dict_friends.items():
    #     dict_friends[k] = sum_bill
    # print(dict_friends)
else:
    print('No one is joining for the party')