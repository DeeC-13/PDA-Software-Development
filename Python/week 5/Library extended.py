
#function to let user borrow or return a book

library = {                             #creates a dictionary of books
    "book 01" : {"title": "IT",
                "author": "Stephen King",
                "available": True},

    "book 02" : {"title": "Beast House",
                "author": "Richard Laymon",
                "available": False},

    "book 03" : {"title": "Relic",
                "author": "Preston & Child",
                "available": False},

    "book 04" : {"title": "Ill Wind",
                "author": "Rachel Caine",
                "available": True},

    "book 05" : {"title": "One Shot",
                "author": "Lee Child",
                "available": True}
}


def display_book_menu():
    print("Menu Options:")
    print("1. Search for a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Admin Options")
    print("Q. Quit")

menu_options = ('1', '2', '3', '4', 'Q', 'q')



def add_book(library):
    title = input(f"Please add book title: ")
    author = input(f"Please add book author: ")
    available = input(f"Please add available True/False: ")

    value = "5"

    finalMessage = f"book {0}"  #increments the last outer key by 1
    for x in range (0, len(value)):
        finalMessage+=(chr(ord(value[x])+1))
        new_book = {finalMessage: {"title": title, "author": author, "available": available}}

        library.update(new_book)    #updates the library with the new book

    print(f"Book '{title}' by {author} has been added to the catalogue with availability {available}")

    print(library)


def add_value(library):
    chosen_book = input("Please choose a book to add genre. Enter book and then the number i.e book 01: ")
    b_genre = input("Please add the genre: ")
    library[chosen_book]["genre"] = b_genre
    print(library)


def delete_book(library):
    d_book = input("Would you like to delete a dook y/n: ")
    if d_book == 'y':
        book_del = input(f"Please choose which book to delete. Please enter book then number i.e book 01: ")
        del library[book_del]
        for book_del, info in library.items():
            if book_del == library.keys() :
                print(f"Book ',{book_del},' has been deleted")


def get_choice(library):

    global value
    display_book_menu()     #calls the menu function

    while True:     #loops while is true

        choice = input("please choose an option between one and four or enter Q to Exit: ") #asks user for input

        if choice in menu_options:  #iterates through user choice to see is in menu

            if choice == '1':

                for book, info in library.items():  # checks user choice and tells user is/not in stock
                    print(f"{book} is {info["title"]} by {info["author"]}")

            elif choice == '2':
                book = input("choose a book: ")
                for value, title in library.items():    #check user choice and checks if the book is in the library
                    if book in value:                   #then tells the user which book they have chosen
                        print("You have chosen ", library[value]["title"])
                        break

                if value in library:
                    if library[value]["available"] == True:

                        for value, title in library.items():  # check user choice and checks if the book is in
                            if book in value:                   #the library
                                print(f"Book ", library[value]["title"] ,"checked out successfully.")
                                library[value]["available"] = False  #changes available to false

                    else:
                        print("Sorry, the book is currently checked out.")

                else:
                   print("Book not fount in the catalogue.")     #output if book is not found in the library

            elif choice == '3':
                book = input("Enter a book to return: ")    #asks user to say which book they are returning
                for value, title in library.items():        #then checks to see if it's listed in the library
                    if book in value:
                        print("You have chosen ", library[value]["title"])#tells the user which book they are returning
                        break

                if value in library:         #checks the book and returns it to the library as available again
                    if value in library:
                        if not library[value]["available"]:
                            library[value]["available"] = True
                            for value, title in library.items():  # check user choice and checks if the book is in
                                if book in value:                   #the library
                                    print(f"Book '{library[value]["title"]}' checked in successfully.")

                        else:
                            print("The book is already available in the library.")

            elif choice == '4':
                new = input("Would you like to add a book? please enter y/n: ")
                if new == 'y':
                    add_book(library)
                elif new == 'n':
                    g_add = input("Would you like to add the genre enter y/n: ")
                    if g_add == 'y':
                        add_value(library)
                    else:
                        delete_book(library)

            else:
                print("Have a good day! ")      #output for quit
                break

        if choice not in menu_options:      #checks user choice is valid. If not asks user to try again
          print("Invalid option please try again")

get_choice(library)
