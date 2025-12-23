user = []
options = ('1', '2', '3', '4', '5')

user_input = str(input("Please enter a sentence: \n"))
user.append(user_input)


def menu():
    print("** Menu Options **")
    print("1. Show the words")
    print("2. Count the words")
    print("3. Reverse the sentence")
    print("4. Count the number of the same letter")
    print("5. Press Q to exit")


def show_words(user):
    print(user)


def count_words(user):
    for i in user:
        print(f"There are ",len(i.split()), "words in your sentence")


def rev_input(user):
    user_rev = [i[::-1] for i in user]
    print("The sentence reversed is",user_rev)


def count_letters(user):
    letter = str(input("Which letter would you like to count?"))
    count = sum(word.count(letter) for word in user)
    print(letter, "appears",count,"times in the sentence")


def main():
    menu()
    get_choice(options)


def get_choice(options):
    global user

    while True:
        user_choice = input("\nPlease choose an option : ")

        if user_choice in options:  #iterates through user choice to see is in menu

            if user_choice == '1':
                show_words(user)

            elif user_choice == '2':
                count_words(user)

            elif user_choice == '3':
                rev_input(user)

            elif user_choice == '4':
                count_letters(user)

            elif user_choice == '5':
                print("Have a good day!")
                quit()

        if user_choice not in options:      #checks user choice is valid. If not asks user to try again
          print("Invalid option please try again")


if __name__ == "__main__":
    main()







