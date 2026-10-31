import json
import os

Manager = {
    'name': 'erfan',
    'pass_word': '1234'
}

if os.path.exists('Employee.json'):
    with open('Employee.json', 'r') as f:
        Employee = json.load(f)
else:
    Employee = []


def save_data():
    with open('Employee.json', 'w') as f:
        json.dump(Employee, f, indent=4)


def add_employee():
    username = input('Enter employee username: ')
    password = input('Enter employee password: ')

    for emp in Employee:
        if emp['user_name'] == username:
            print('Username already exists!')
            return

    Employee.append({
        'user_name': username,
        'pass_word': password
    })

    save_data()
    print('Employee added successfully!')


def show_employees():
    if not Employee:
        print('No employees found.')
        return

    for emp in Employee:
        print('Username:', emp['user_name'])



name = input('Enter your name: ')
password = input('Enter your password: ')

if name == Manager['name'] and password == Manager['pass_word']:

    while True:
        print('\n1. Add new employee')
        print('2. Show employees')
        print('3. Exit')

        choice = input('Choose: ')

        if choice == '1':
            add_employee()

        elif choice == '2':
            show_employees()

        elif choice == '3':
            print('Goodbye!')
            break

        else:
            print('Invalid choice!')

else:
    print('Username or password is incorrect!')
