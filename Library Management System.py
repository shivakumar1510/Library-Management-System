class Book:
    def __init__(self, book_id, title, author, isbn, quantity):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity

class Patron:
    def __init__(self, patron_id, name, contact_info, membership_type):
        self.patron_id = patron_id
        self.name = name
        self.contact_info = contact_info
        self.membership_type = membership_type

class Loan:
    def __init__(self, loan_id, patron, book, loan_date, due_date):
        self.loan_id = loan_id
        self.patron = patron
        self.book = book
        self.loan_date = loan_date
        self.due_date = due_date
        self.return_date = None

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}
        self.loans = {}
        self.book_id_counter = 1
        self.patron_id_counter = 1
        self.loan_id_counter = 1

    def add_book(self, title, author, isbn, quantity):
        book_id = self.book_id_counter
        self.books[book_id] = Book(book_id, title, author, isbn, quantity)
        self.book_id_counter += 1

    def add_patron(self, name, contact_info, membership_type):
        patron_id = self.patron_id_counter
        self.patrons[patron_id] = Patron(patron_id, name, contact_info, membership_type)
        self.patron_id_counter += 1

    def borrow_book(self, patron_id, book_id, loan_date, due_date):
        patron = self.patrons.get(patron_id)
        book = self.books.get(book_id)

        if patron and book and book.quantity > 0:
            loan_id = self.loan_id_counter
            self.loans[loan_id] = Loan(loan_id, patron, book, loan_date, due_date)
            book.quantity -= 1
            self.loan_id_counter += 1
            return loan_id

    def return_book(self, loan_id, return_date):
        loan = self.loans.get(loan_id)

        if loan and not loan.return_date:
            loan.return_date = return_date
            book = loan.book
            book.quantity += 1

    def get_books(self):
        return self.books.values()

    def get_patrons(self):
        return self.patrons.values()

    def get_loans(self):
        return self.loans.values()


# Example usage
library = Library()

library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0", 5)
library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", 3)

library.add_patron("John Doe", "john@example.com", "Regular")
library.add_patron("Jane Smith", "jane@example.com", "Premium")

loan_id = library.borrow_book(1, 1, "2023-08-01", "2023-09-01")
library.return_book(loan_id, "2023-08-20")

for book in library.get_books():
    print(f"Book: {book.title}, Available Quantity: {book.quantity}")

for patron in library.get_patrons():
    print(f"Patron: {patron.name}, Membership: {patron.membership_type}")

for loan in library.get_loans():
    print(f"Loan: Patron: {loan.patron.name}, Book: {loan.book.title}, Due Date: {loan.due_date}, Returned: {loan.return_date}")
