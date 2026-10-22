class Book():
    def __init__(self, title, subject):
        self.title = title
        self.subject = subject

    def __str__(self):
        return f'Title: {self.title} | Subject: {self.subject}'

def show_all_books():
    for n, item in enumerate(books):
        print(f"{n + 1}. {item}")

def is_empty():
    if  not books:
        print("We don't have book! ")
        return True
    return False

books = []

while True:
    try:
        choose = int(input('\n0. Stop | 1. Add | 2. Remove | 3. Edit | 4. List | 5.search book\nEnter your choice: ').strip())
        
        if 0 <= choose <= 5:
            if choose == 0:
                print('Exiting program. Goodbye!')
                break
                
            elif choose == 1:
                title = input('Enter book title: ').strip()
                subject = input('Enter book subject: ').strip()
                book = Book(title, subject)
                books.append(book)
                print('Book added successfully!')
                
            elif choose == 2:
                if is_empty():
                    continue
                
                show_all_books()
                num = int(input('Enter book number to remove: ').strip())
                if 1 <= num <= len(books):
                    books.pop(num - 1)
                    print('Book removed successfully!')
                else:
                    print(f'Please enter a number between 1 and {len(books)}.')

            elif choose == 3:
                if is_empty():
                    continue
                show_all_books()
                num = int(input('Enter book number to edit: ').strip())

                if 1 <= num <= len(books):
                    title = input('Enter new book title: ').strip()
                    subject = input('Enter new book subject: ').strip()
                    book = books[num - 1]
                    book.title = title
                    book.subject = subject
                    print('Book edited successfully!')
                else:
                    print(f'Please enter a number between 1 and {len(books)}.')

            elif choose == 4:
                if is_empty():
                    continue
                print('\n--- Book List ---')
                show_all_books()

            elif choose==5:
                if is_empty():
                    continue

                title=input('Enter book title: ').strip()
                found = False

                for book in books:
                    if book.title.lower() == title.lower():
                        print(book)  
                        found = True  

                if not found:
                    print("We don't have a book with this title name! ")

        else:
            print('Invalid choice! Please enter a number between 0 and 5.')

    except ValueError:
        print('Invalid input! Please enter a valid number.')
