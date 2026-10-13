students=[]
while True:
    try:
        choose=int(input('0.stop  1.add  2.remove \n '))
        if choose not in [1,2,0]:
            print('enter number 1,2,0')
            continue
        if choose==0:
            break
        elif choose==1:
            name=input('Enter student name: ')
            students.append(name)
            for i in students:
                print(i)

        elif choose == 2:
            if len(students) > 0:
                for i in students:
                    print(i)

                name = input('Enter student name: ')

                if name in students:
                    students.remove(name)
                    print('Student removed successfully!')
                else:
                    print('We don’t have a student by that name')

                for i in students:
                    print(i)

            else:
                print('We don’t have any students')

    except ValueError:
        print('try ageen!')