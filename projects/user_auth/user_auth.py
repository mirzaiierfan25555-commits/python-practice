users={
    'erfan': '123',
    'amir': '1234',
    'reza': '12345'
}

user_name=input('Enter your user name: ')
pass_word=input('Enter your pass word: ')

if user_name in users and users[user_name]==pass_word:
    print('welcom',user_name)
else:
    print("Invalid username or password.")