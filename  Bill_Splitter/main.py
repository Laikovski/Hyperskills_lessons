# Stage 1/4: Invite your friends
print('Enter the number of friends joining (including you):')
count_friends = int(input())
print('')
dict_friends = {}
if count_friends > 0:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(count_friends):
        dict_friends[input()] = 0
    print('')
    print(dict_friends)
else:
    print('No one is joining for the party')