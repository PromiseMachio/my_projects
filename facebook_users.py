#Below code shows online and offline users in facebook.
users = {'Machio':'online','Peter':'offline','Derric':'online',
         'Jane':'offline','Hassan':'offline','Jessica':'online'}
#Strategy 1; iterate over copy
for user, status in users.copy().items():
    if status == 'offline':
        del users[user]

#strategy 2; creating a new collection of those online
online_users = {}
for user, status in users.items():
    if status  == 'online':
        online_users[user] = status
print(online_users)
