import datetime

#Section 1
#Function to take a list of numbers and return the sum
nums_list = []


def get_nums():
    nums_l = 5

    #asks user for 5 numbers
    for i in range(nums_l):
        nums_l = float(input("Please enter a number. Enter a number only: "))
        nums_list.append(nums_l)

    #returns users numbers in a list
    return nums_list


print("Your numbers are ", get_nums())

#adds users numbers together and displays total
total = sum(nums_list)


print("The total of your numbers is: ", total)


#Function to count the number of vowels in a string


def get_vowels():
    vowels = 'aeiou'
    count = 0

    #asks user to input a sentence
    say = str(input("Please enter a sentence: "))

    #checks the sentence for vowels and counts them
    for char in say:
        if char in vowels:
            count += 1

    #returns number of vowels
    return count


print("The number of vowels is: ", get_vowels())

#Funtion to get max from three numbers

get_nos = []


def max_num():
    get = 3

    #asks user to input three numbers
    for i in range(get):
        get = int(input("Please enter a whole number: "))
        get_nos.append(get)

    #returns the three numbers
    return get_nos


print("Your numbers are: ", max_num())

#gets the maximum number from the three numbers
maxno = max(get_nos)


print("The largest number in your numbers is: ", maxno)


#Section 2

#1. function that asks the user for their age and then calculates how long till they retire
#asks the user to input their birth year
year = int(input('Enter your year of birth in yyyy format: '))


def age(year):

    now = datetime.datetime.now() #gets today's date
    current_year = now.year #sets current year as variable
    current_age = current_year - year #finds the difference between current and birth year

    #returns the difference plus 1 year for the next birthday age
    return current_age + 1


print(f"You will be ", age(year), "on your birthday")

result = age(year)


def retire(result):
    #uses the age from the previous function and minuses from retirement age
    retire_age = result
    x = 68
    y = retire_age
    a = x - y

    #returns difference
    return a


print("You have ", retire(result), "years till retirement")

#Usier input for calculating amount of grit needed
size = int(input("How big is your driveway in square metres? enter numbers only: "))

minimum = 10
maximum = 15


def calculate_amount(minimum, maximum):
    #calculates the maximum and minimum amount of gravel needed from users input size
    min_amount = round(size / minimum, 2)
    max_amount = round(size / maximum, 2)

    return min_amount, max_amount


print("The min/maxamount of grit need is ", calculate_amount(minimum, maximum), "grams per square metre")

#Temperature app based on user input
temp_list = []


def get_temps(temp_list):
    list_t = 7

    #asks the user for seven temperatures
    for i in range(list_t):
        temp = float(input("Please enter the measured temperature today. Enter number only: "))
        temp_list.append(temp)

    #returns users temperatures
    return temp_list


print("The temperatures for ", datetime.datetime.now(), "are ", get_temps(temp_list))

calc_temps = temp_list

max_value = max(calc_temps) #calculates maximum temperature

min_value = min(calc_temps) #calculates minimum temperature

ave_value = round(sum(temp_list) / len(temp_list), 2)   #calculates the average temperature

print("The maximum temperature for today is: ", max_value)

print("The minimum temperature for today is: ", min_value)

print("The average temperature for today is: ", ave_value)

# prints out the statement from the average temperature
if ave_value >= 19:
    print("It has been hot!")
elif 11 <= ave_value < 18:
    print("It has been nice and warm")
elif 6 <= ave_value <= 10:
    print("It has been mild")
else:
    print("It's not been too bad")

#Function for a menu with three items

#functions to store options as variables
def option_1():
    option1 = 1
    print("You chose option:  ", option1)


def option_2():
    option2 = 2
    print("You chose option:  ", option2)


def option_3():
    option3 = 3
    print("You chose option:  ", option3)


def option_4():
    option4 = "Q"
    print("You chose to Quit:  ", option4, "\n Have a great day!")
    quit()


def display_menu():
    print("Menu Options:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("Q. Quit")

#stores the options as a list
options = ('1', '2', '3', 'Q', 'q')


def get_choice():
    display_menu()
    while True:

        #asks user to choose an option
        choice = input("please choose an option between one and three or enter Q to Exit: ")

        #input validation for user choice
        if choice in options:

            #calls the relevant function for the users choice
            if choice == '1':
                option_1()
            elif choice == '2':
                option_2()
            elif choice == '3':
                option_3()
            else:
                option_4()

        #assesses to see if the users choice is in the options and if not prompts them to try again
        if choice not in options:
          print("Invalid option please try again")

get_choice()


#function to let user borrow or return a book

library = {                             #creates a dictionary of books
    "book1" : {"title": "IT",
                "author": "Stephen King",
                "available": True},

    "book2" : {"title": "Beast House",
                "author": "Richard Laymon",
                "available": False},

    "book3" : {"title": "Relic",
                "author": "Preston & Child",
                "available": False},

    "book4" : {"title": "Ill Wind",
                "author": "Rachel Caine",
                "available": True},

    "book5" : {"title": "One Shot",
                "author": "Lee Child",
                "available": True}
}


def display_book_menu():
    print("Menu Options:")
    print("1. Search for a book")
    print("2. Borrow a book")
    print("3. Return a book")
    print("Q. Quit")

menu_options = ('1', '2', '3', 'Q', 'q')


def get_choice():

    global value
    display_book_menu()     #calls the menu function

    while True:     #loops while is true

        choice = input("please choose an option between one and three or enter Q to Exit: ") #asks user for input

        if choice in menu_options:  #iterates through user choice to see is in menu

            if choice == '1':

                for book, info in library.items():      #checks user choice and tells user is/not in stock
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

            else:
                print("Have a good day! ")      #output for quit
                break

        if choice not in menu_options:      #checks user choice is valid. If not asks user to try again
          print("Invalid option please try again")

get_choice()





