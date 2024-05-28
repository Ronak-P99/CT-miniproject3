import re
from Book_operation import BookOperation, Book
from Book_operation import UserOperation, User
from Book_operation import AuthorOperation, Author
from Book_operation import GenreOperation, Genre

def main():
    book_inst = BookOperation()
    user_inst = UserOperation()
    author_inst = AuthorOperation()
    genre_inst = GenreOperation()
    while True:
        try:
            action = int(input("\nWlecome to the Library Management System!\n\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Genre Operations\n5. Quit\nChoose the number you would like: "))
            if action not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid action.")
            
            #!!BOOK OPERATION!!

            if action == 1:
                try:
                    while True:
                        print("Book Operations:\n\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books\n6. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4, 5]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please enter the name of the book: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            author = input("Please enter the name of the author: ")
                            if all([letter.isalpha() or letter.isspace() for letter in author]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            isbn = input("Please enter the ISBN of the book (Do not format!): ")
                            try:
                                int(isbn)
                                formatted_isbn = re.sub(r'(\d{3})(\d{10})', r'\1-\2', isbn)
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            genre = input("Please enter the genre of the book: ")
                            if all([letter.isalpha() or letter.isspace() for letter in genre]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            date = input("Please enter the date the book was published (Do not format!): ")
                            try:
                                int(date)
                                formatted_date = re.sub(r'(\d{2})(\d{2})(\d{4})', r'\1/\2/\3', date)
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            status = 'Available'
                            book_inst.add_book(Book(name, author, formatted_isbn, genre, formatted_date), status)
                        elif action == 2:
                            name = input("Enter book name to borrow: ")
                            book_inst.borrow_book(name)
                        elif action == 3:
                            name = input("Enter book name to return: ")
                            book_inst.return_book(name)
                        elif action == 4:
                            name = input("Enter the name of the book you would like to search for: ")
                            book_inst.search_book(name)
                        elif action == 5:
                            book_inst.display_books()
                        elif action == 6:
                            break
                except ValueError as e:
                    print(e)

            #!!USER OPERATION!!

            if action == 2:
                try:
                    while True:
                        print("\nUser Operations\n1. Add a new user\n2. View user details\n3. Display all users\n4. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please enter the name of the user: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            lib_id = input("Please enter the 10 digit library ID: ")
                            try:
                                if len(lib_id) == 10:
                                    int(lib_id)
                                else:
                                    print("Library ID needs to be a length of 10!")
                                    break
                            except ValueError:
                                print("This is not a number. Try again")
                                break
                            borrowed_books = []
                            while True:
                                book = input("What books has the user borrowed? Type 'Stop' once done listing! ")
                                if book.lower() != 'stop':
                                    borrowed_books.append(book) 
                                else: 
                                    break     
                            user_inst.add_user(User(name, lib_id, borrowed_books))
                        elif action == 2:
                            user_input = input("What is the name of the person you would like to see the details of? (Please make sure to type it exactly as in the system!): ")
                            user_inst.view_user(user_input)
                        elif action == 3:
                            user_inst.view_all()
                        elif action == 4:
                            break
                except ValueError as e:
                    print(e)

            #!!Author Operations!!

            if action == 3:
                try:
                    while True:
                        print("\nAuthor Operations\n1. Add a new author\n2. View author details\n3. Display all authors\n4. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please enter the name of the author: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            author_biography = input("Please enter a brief description of the author in 250 chars or less.\n")
                            if len(author_biography) >= 251:
                                print("Please make sure the biography is less than 250 characters!")
                                break
                            author_inst.add_author(Author(name, author_biography))
                        elif action == 2:
                            author_input = input("What is the name of the author you would like to see the details of? (Please make sure to type it exactly as in the system!): ")
                            author_inst.view_author(author_input)
                        elif action == 3:
                            author_inst.view_all_author()
                        elif action == 4:
                            break
                except ValueError as e:
                    print(e)

            #!!Genre Operations!!

            if action == 4:
                try:
                    while True:
                        print("\nGenre Operations\n1. Add a new genre\n2. View genre details\n3. Display all genres\n4. Main Menu")
                        action = int(input("Please choose the number that you want to do: "))
                        if action not in [1, 2, 3, 4]:
                            raise ValueError("Invalid action.")
                        if action == 1:
                            name = input("Please give the name of book for the genre: ")
                            if all([letter.isalpha() or letter.isspace() for letter in name]):
                                pass
                            else:
                                print("Only letters are allowed! Try again")
                                break
                            genre_description = input("Please enter a brief description of the genre in 100 characters or less.\n")
                            if len(genre_description) >= 101:
                                print("Please make sure the description is less than 100 characters!")
                                break
                            categories = ['HORROR', 'THRILLER', 'COMEDY', 'FANTASY', 'ACTION', 'DRAMA']
                            category = input("Choose the category out of this list: Horror, Thriller, Comedy, Fantasy, Action, Drama: ")
                            if category.upper() in categories: 
                                genre_inst.add_genre(Genre(name, genre_description, category))
                            else:
                                print("The category you provided was not in the list. Please try again.")
                                break
                        elif action == 2:
                            name = input("Please give the name of the book to check the genre. (Please make sure to type it exactly as in the system!): ")
                            genre_inst.view_genre(name)
                        elif action == 3:
                            genre_inst.view_all_genres()
                        elif action == 4:
                            break
                except ValueError as e:
                    print(e)
            
            if action == 5:
                break
                
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()