
import datetime

while True:
    try:
        choice = input(
            '\n1. Add student name\n'
            '2. Show students name\n'
            '3. Stop\n'
            'Choose an option: '
        )

        if choice == '3':
            print('Goodbye!')
            break

        elif choice == '1':
            while True:
                name = input('Enter student name (exit to stop): ')

                if name.lower() == 'exit':
                    break

                if not name.strip():
                    print('Name cannot be empty!')
                    continue

                filename = str(datetime.date.today()) + '.txt'

                with open(filename, 'a') as f:
                    f.write(f'Name: {name}\n')

                print('Student added successfully!')

        elif choice == '2':
            date = input('Enter date (YYYY-MM-DD): ')
            filename = date + '.txt'

            try:
                with open(filename, 'r') as f:
                    print('\n' + f.read())

            except FileNotFoundError:
                print('File not found!')

        else:
            print('Invalid option!')

    except ValueError:
        print('Invalid input!')
