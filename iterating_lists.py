#!/usr/local/bin/python3.7

#user = { 'admin': True, 'active': True, 'name': 'Kevin' }
#user = { 'admin': False, 'active': False, 'name': 'Kevin' }

users = [ { 'admin': False, 'active': True, 'name': 'Kevin' },
          { 'admin': True, 'active': True, 'name': 'Toto' },
          { 'admin': False, 'active': False, 'name': 'Titi' }
        ]

line = 1
for user in users:
    if user['admin'] == True and user['active'] == True:
        print(f"{line} ACTIVE- (ADMIN) {user['name']}")
        line += 1
    elif user['admin'] == True:
        print(f"{line} (ADMIN) {user['name']}")
        line += 1
    elif user['active'] == True:
        print(f"{line} ACTIVE- {user['name']}")
        line += 1
    elif user['admin'] != True and user['active'] != True:
        print(f"{line} {user['name']}")
        line += 1
