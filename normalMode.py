from colorama import Fore

class NormalMode(object):
    def play_game(self, secret_word):

        word = secret_word['word']
        word = word.strip().lower()  # removes whitespaces and uppercase
        mistakes = 0  # Number of mistakes. When it reaches 6 it's game over.
        guesses = []  # stores the wrong guesses of the player
        player = []
        replace = [" ","'","=","-","!",":",",","?",";","(",")"] # replaces these symbols from the word
        for i in word:
            if i in replace:
                player.append(i)
            else:
                player.append("_")
        # player is initialized with as manys "_" as the legth of the word
        victory = False  # marks the player's victory

        print(Fore.LIGHTYELLOW_EX, "The game is about to start!\n\n")

        while mistakes is not 5 and not victory:
            print(Fore.LIGHTYELLOW_EX, "\n\nThe hint is: " + secret_word['hint1'] + ".")
            if mistakes > 3:
                print(Fore.LIGHTYELLOW_EX, "Another hint: " + secret_word['hint2'] + ".")

            show_wrong(guesses)
            show_tries(mistakes)
            show_word(player)

            try:
                letter = player_input()

                if letter in word:
                    print(Fore.LIGHTGREEN_EX, "Nice! '" + letter.upper() + "' is in the word.")
                    player_right(letter, player, word)
                else:
                    if letter not in guesses:
                        print(Fore.LIGHTRED_EX, "Wrong! '" + letter.upper() + "' is not in the word.")
                        guesses.append(letter)
                        mistakes += 1
                    else:
                        print(Fore.LIGHTRED_EX, "C'mon, don't make the same mistake twice. ರ_ರ")
            except:
                print(Fore.LIGHTRED_EX, "Invalid Input!")

            victory = "_" not in player  # checks for victory

        if victory:
            show_word(player)
            print(Fore.LIGHTMAGENTA_EX, "\n\nCongratulations! You Won!")
            print("The word is " + word.title())
        else:
            show_word(player)
            print(Fore.LIGHTRED_EX, "\n\nYou lost! Better luck next time!")
            print("The word is " + word.title())

        print("\n>>>Back to Main Menu  三三ᕕ( ⌓̈ )ᕗ\n")


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
    if not player[0].isnumeric():
        player[0] = player[0].upper()
    print(Fore.LIGHTCYAN_EX, "The word looks like this:\n  ", end="")
    for i in player:
        if i == " ":
            print(Fore.LIGHTWHITE_EX, " ", end="")
        else:
            print(Fore.LIGHTWHITE_EX, i, end="")
