options = ('1', '2', '3', '4', '5')

user_input = input("Please enter a sentence: \n").lower()
words = user_input.split()
word_dict = {i: word for i, word in enumerate(words)}


def menu():
    print("** Menu Options **")
    print("1. Show the words")
    print("2. Count the words")
    print("3. Reverse the sentence")
    print("4. Count the number of the same letter")
    print("5. Press Q to exit")


def show_words():
    for value in word_dict.values():
        print(value)


def count_words(word_dict):
    count = len(word_dict)      #counts the length of the dictionary
    print(f"There are ",count, "words in your sentence")    #displays the count of the dictionary


def rev_input(word_dict):
    reversed_dict = {v: k for k, v in word_dict.items()}    #reverses the dictionary

    for key, value in reversed(reversed_dict.items()):  # Print values in reverse order
        print(key)


def count_letters(word_dict):
    letter = str(input("Which letter would you like to count?")).lower()
    letter_count = user_input.count(letter)
    print(letter, "appears",letter_count,"times in the sentence")


def main():
    menu()
    get_choice(options)


def get_choice(options):
    global word_dict

    while True:
        user_choice = input("\nPlease choose an option : ")

        if user_choice in options:  #iterates through user choice to see is in menu

            if user_choice == '1':
                show_words()

            elif user_choice == '2':
                count_words(word_dict)

            elif user_choice == '3':
                rev_input(word_dict)

            elif user_choice == '4':
                count_letters(word_dict)

            elif user_choice == '5':
                print("Have a good day!")
                quit()

        if user_choice not in options:      #checks user choice is valid. If not asks user to try again
          print("Invalid option please try again")


if __name__ == "__main__":
    main()







