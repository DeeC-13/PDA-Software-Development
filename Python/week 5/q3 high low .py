import random

count = 1
max_count = 10
result = [0,1,2]

comp = int(random.randrange(1, 100))


def comp_guess():
    return comp


def menu():
    print("Welcome to the High Low Game")
    print("To play you need to guess the correct number")
    print("You have 10 chance to get it right")
    print("Good Luck and happy playing!")
menu()


def check_number(player):
    while True:

        try:
            if player.is_integer() and 1 <= player <= 100:
                break

            else:
                print("Please enter a number between (1-100)")
                main()

            if player is not int:
                break

            elif not player:
                break

        except ValueError:
            print("Invalid input. Please try again")


def main():
    game(comp)
    count_round()


def game(comp):
    global count, result

    player = int(input("Pick a number between 1 and 100: "))
    check_number(player)

    while True:

        if player < comp:
            result = 0
            get_result()
            break


        elif player > comp:
            result = 1
            get_result()
            break

        else:
            end()


def count_round():
    global count
    while True:
        if count < max_count:
            print("Round",count, "of", max_count)
            count +=1
            game(comp)

        else:
            end()
            break


def get_result():

    if result == 0:
        print("Guess a higher number")

    elif result == 1:
        print("Guess a lower number")

    else:
        end()


def end():
    global count

    if count < max_count:
        print("You have guessed in",count, "rounds")
        quit()

    elif count == max_count:
        print("Game Over!")
        print("You did not guess the number")
        quit()


if __name__ == "__main__":
    main()