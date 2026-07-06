
def get_sentence():

    while True:

        sentence = input("Please enter a sentence: ")

        if sentence != "":
            return sentence

        print("Please enter letters only.")


def get_vowels():

    vowels = "aeiou"
    count = 0

    sentence = get_sentence()

    for char in sentence.lower():

        if char in vowels:
            count += 1

    return count


print("Number of vowels:", get_vowels())