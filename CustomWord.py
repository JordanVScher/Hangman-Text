import getpass
from colorama import Fore


class CustomWord(object):
    def play_game(self):
        word, hint = enter_word()

        word = word.strip().lower()  # removes whitespaces and uppercase
        mistakes = 0  # Number of mistakes. When it reaches 6 it's game over.
        guesses = []  # stores the wrong guesses of the player
        player = ["_" for i in word]  # stores the right guesses of the player
        # player is initialized with as manys "_" as the legth of the word
        victory = False  # marks the player's victory

        print(Fore.LIGHTYELLOW_EX, "The game is about to start!\n\n")

        while mistakes is not 5 and not victory:
            print(Fore.LIGHTYELLOW_EX, "\n\nThe hint is : " + hint + ".")
            show_wrong(guesses)
            show_tries(mistakes)
            show_word(player)
            letter = player_input()

            if letter in word:
                print("Nice! '" + letter.upper() + "' is in the word.")
                player_right(letter, player, word)
            else:
                if letter not in guesses:
                    guesses.append(letter)
                    mistakes += 1
                else:
                    print(Fore.LIGHTRED_EX, "C'mon, don't make the same mistake twice. ರ_ರ")

            victory = "_" not in player  # checks for victory

        if victory:
            print(Fore.LIGHTMAGENTA_EX, "\n\nCongratulations! You Won!")
            print("The word is " + word.capitalize())
        else:
            print(Fore.LIGHTRED_EX, "\n\nYou lost! Better luck next time!")
            print("The word is " + word.capitalize())

        print(">>>Back to Main Menu  三三ᕕ( ⌓̈ )ᕗ\n")


def player_input():
    print(Fore.LIGHTYELLOW_EX, "\n\nEnter a letter")
    letter = input("-->")
    letter = letter.strip().lower()  # removes whitespaces and uppercase
    return letter[0]


def player_right(letter, player, word):
    index = 0
    for i in word:
        if letter == i:
            player[index] = letter
        index += 1


def show_wrong(guesses):
    print("Your mistakes:", end="")
    for i in guesses:
        print(" " + i, end="")


def show_tries(mistakes):
    if mistakes == 4:
        print(Fore.LIGHTRED_EX, "\nYou only have 1 try! Good luck!")
    else:
        print("\nYou have " + str(5 - mistakes) + " tries")


def show_word(player):  # print the players guesses in a nice manner
    player[0] = player[0].upper()
    print(Fore.LIGHTCYAN_EX, "The word looks like this:\n  ", end="")
    for i in player:
        print(Fore.LIGHTWHITE_EX, " " + i, end="")


def enter_word():
    # a and b are used to confirm the word
    a = ""
    b = " "
    while a is not b:
        print(Fore.LIGHTMAGENTA_EX, "\n Insert the word you want.")
        a = getpass.getpass(" Don't worry, it's hidden!")
        print("*" * len(a))
        b = getpass.getpass(" Reinsert the word to make sure the spelling is correct:")
        print("*" * len(b))
        if a == b:
            break
        print(Fore.LIGHTRED_EX, "The words don't match! Try again! ")

    if not a:  # just a little easter egg in case the user inputs a blank word
        # inspired by The Crying of Lot 49
        a = "Tristero"
        h = "We await silent ________'s empire"
    else:
        print("Great! Now enter a hint: ")
        h = getpass.getpass("It can be blank if you want...\n")
        if not h:
            h = "empty"

    print("Sucess!")
    return a, h

