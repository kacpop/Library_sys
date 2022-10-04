# We are creating simple system for library
# It have to implement functions: add book copy, borrow a copy, give back a copy.
# Borrower can only have max 3 copies of books.

#Creating book class. It contains list of copies of that book
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.copies = []
    def __str__(self):
        return self.title +'/'+ self.author 
    
    def __eq__(self, other):
        return (self.title == other.title) and (self.author == other.author)

class Copy():
    def __init__(self,title,author, published):
        self.title = title
        self.author = author
        self.published = published

    def __str__(self):
        return self.title +'/'+ self.author

#Burrower class contains books borrowed by instance of this class
class Borrower:
    def __init__(self, surname):
        self.surname = surname
        self.borrowed_books = []

#main library class
class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []
    
    # function that checks if book exists in the library. Returns true if exists and adds copy to list of copies. Return false if there is no book in the library
    # function is used in add_book function. Does not work independently.
    def add_copy(self, title,author, copy):
        for boook in self.books:
            if boook.title == title and boook.author == author:
                boook.copies.append(copy)
                return True
        return False

    #Checks if borrower is listed in library. Returns borower if True, creates new borower if flase.
    # Help class. Is used in borrow_book function.
    def check_borrower(self, surname):
        for borrrower in self.borrowers:
            if borrrower.surname == surname:
                print('Borrower is in database')
                return borrrower
        borrower = Borrower(surname)
        print('borrower created')
        self.borrowers.append(borrower)
        return borrower

    # Function tries to remove copy of book from library and adds it to borrower
    # Help class. Is used in borrow_book function.
    def check_book(self, title, borrower):
        war1=False
        war2=False
        if len(borrower.borrowed_books) < 3:
            for boook in self.books:
                if boook.title == title:
                    war2=True
                    if len(boook.copies) > 0:
                        war1=True
                        borrower.borrowed_books.insert(0, boook.copies.pop(0))
                        print('Book borrowed. Borrower now have: ' + borrower.borrowed_books[0].title)
                        return True
            if war2 == False: print('Library does not have this book available')
            elif war1 == False: print('Library does not have copy of this book available')
        else: print('Borrower already has 3 books. Action cannot be executed')


    # adds book and copy to library
    def add_book(self, title, author, published):
        copy = Copy(title, author, published)
        if self.add_copy(title, author, copy) == True:
            print('Book was in the library. Copy added')
        else:
            book = Book(title,author)
            book.copies.append(copy)
            self.books.append(book)
            print('Book was not in the library. Book and copy added')

    #borrows copy to borrower
    def borrow_book(self, title, borrower):
        person = self.check_borrower(borrower)
        self.check_book(title, person)

    #Function shows which books are available to borrow
    def show_books(self):
        for boook in self.books:
            if len(boook.copies) != 0:
                print(boook)
    #Function shows which books are borrowed now and shows borrower
    def show_borrowed_books(self):
        for borrower in self.borrowers:
            for book in borrower.borrowed_books:
                print(borrower.surname, book)
    
    # Tries to remove copy from borrower and adds it to library
    def return_book(self, title, surname):
        con1 = False
        con2 = False
        for borrower in self.borrowers:
            if borrower.surname == surname:
                con1 = True
                for borrowed_book in borrower.borrowed_books:
                    if borrowed_book.title == title:
                        con2 = True
                        for library_book in self.books:
                            if library_book.title == title:
                                library_book.copies.insert(0, borrower.borrowed_books.pop(borrower.borrowed_books.index(borrowed_book)))
                                print('Book returned')
        if con1 == False: print('Borrower is not in database')
        elif con2 == False: print('Borrower does not have this book')




        
library = Library()

actions = int(input())
for i in range(0, actions):
  print('Choose next action: add, borrow, return, show_borrowed, show_books')
  action = input()
  if action =="borrow":
    print('Enter title')
    title = input()
    print('Enter your surname')
    surname = input()
    library.borrow_book(title, surname)
  elif action =="return":
    print('Enter title')
    title = input()
    print('Enter your surname')
    surname = input()
    library.return_book(title, surname)
  elif action == "add":
    print('Enter title')
    title = input()
    print('Enter author')
    author = input()
    print('Enter year of publication')
    published = input()
    library.add_book(title, author, published)
  elif action == "show_borrowed":
    library.show_borrowed_books()
  elif action == "show_books":
    library.show_books()
print('Program ends')


