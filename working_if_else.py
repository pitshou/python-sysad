#!/usr/local/bin/python3.7

#user = { 'admin': True, 'active': True, 'name': 'Kevin' }
user = { 'admin': False, 'active': False, 'name': 'Kevin' }

if user['admin'] == True and user['active'] == True:
    print(f"ACTIVE- (ADMIN) {user['name']}")
elif user['admin'] == True:
    print("(ADMIN) {user['name']}")
elif user['active'] == True:
    print(f"ACTIVE- {user['name']}")
elif user['admin'] != True and user['active'] != True:
    print(f"{user['name']}")
