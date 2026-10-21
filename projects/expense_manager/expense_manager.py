l=[]
def expense_manager():
    while True:
        try:
            choose=int(input('0.stop 1.add  2.list  3.sum  '))
            if choose>3:
                print(f'{choose} is greater than 3')
                continue
            elif choose<0:
                print(f'{choose} is less than 0')
                continue
        except ValueError:
            print('error! Enter just int.')
            continue
        if choose==0:
            break

        elif choose==1:
            category=input('enter category: ')
            expense_input=input('Enter expense: ')
            if expense_input.isdigit():
                expense=int(expense_input)
                d={
                    'expense':expense,
                    'category':category
                }
                l.append(d)
            else:
                print('pleas enter int for expense. ')
                continue
        elif choose==2:
            for e,i in enumerate(l):
                print(e,end='.')
                for key in i:
                    print(key,end=' ')
                    print(i[key])

        elif choose==3:
            total_expense=0
            for i in l:
                total_expense+=i.get('expense')
            print(f'sum= {total_expense}')

expense_manager()
