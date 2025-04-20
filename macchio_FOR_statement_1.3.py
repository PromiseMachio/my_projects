"""
In this project am using the for statement with the funtions ;.copy().items()
this is then followed by the delete function del to remove stored variables.
"""
Users ={'Machio':'Active','Richard':'Active','Felix':'Inactive',
        'Gloria':'Active','Purity':'Active','Promise':'Inactive'}
#Strategy iterate over copy
for User, status in Users.copy().items():
    if status == 'Inactive':
        del Users[User]

#Strategy create a new collection
Active_users = {}
for User, status in Users.items():
    if status == 'Active':
        Active_users[User]=status
