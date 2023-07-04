system_user = {'user_name': 'vannda', 'pwd': 'HappyNewYear', 'age':30}

login_name = input('Please input your username:')
# print(login_name == system_user ['user_name'])

if login_name == system_user['user_name']:
    print('your username is correct.')
else:
    print('your username does not exist, please register again.')