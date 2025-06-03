#This is my code on the above break statement code type.
users = {'Dan':'active','Jane':'inactive','Linda':'active'}
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
#create a new collections
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)

print('---------------------------------------------')
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f"{x} is equals {x} * {n // x}")
print("----------------------------------------------")
