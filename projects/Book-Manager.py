"""
Project: Book Manager
Description: A simple CLI application to manage a book library using OOP principles.
Author: [erfan mirzaii]
Features: Add, Remove, Edit, and List books.
"""


class Book:
    def __init__(self,title,subject):
        self.title=title
        self.subject=subject

    def print(self):
        return(f'{self.title} : {self.subject}')

def print_book_list():
    for i, book in enumerate(books,1):
        res=book.print()
        print(i,res)

def is_empty():
    if  not books:
        print("We don't have book! ")
        return True
    return False
        


books=[]
while True:
    a=input('1.add 2.remove  3.edit  4.print_list  5.stop  : ')
    if a=="5":
        break
    elif a=='1':
        title=input('Enter book title : ')
        subject=input('Enter book Subject : ')
        book=Book(title,subject)
        books.append(book)
        
    elif a=='2':
        if is_empty():
            continue
        print_book_list()
        try:
            num=int(input('Enter item num : '))
            if 1<=num<=len(books):
                books.pop(num-1)
            else:
                print('Invalid number!')
        except ValueError:
            print('you must just enter int')
    elif a=='3':
        if is_empty():
            continue
        print_book_list()
        try:
            num=int(input('Enter item num : '))
            if 1<=num<=len(books):
                book=books[num-1]
                title=input('Enter book title : ')
                subject=input('Enter book Subject : ')
                book.title=title
                book.subject=subject
            else:
                print('Invalid number!')
        except ValueError:
            print('you must just enter int')
    elif a=='4':
        if is_empty():
            continue
        print_book_list()
    
    else:
        continue
