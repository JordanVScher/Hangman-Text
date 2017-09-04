# menu do Jogo da Forca
# Versão Texto
# cd C:\Users\Jordan Victor\PycharmProjects\forcaTexto
# python mainMenu.py
# https://www.npmjs.com/package/cool-ascii-faces
'''Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL'''

from colorama import *
import sys
import os
from CustomWord import *
from normalMode import *
from getWords import *


def check_input(x):  # Checks if user input is valid
    x = x.strip()  # Gets rid of spaces
    # Gets only the first char of the input, if it exists
    if not x:
        print(Fore.LIGHTWHITE_EX, "You have to input something!")
        return False
    else:
        x = x[0]
        if x.isnumeric() and int(x) >= 1 and int(x)<= 4:
            return True
        else:
            return False

def overMenu(user): # the options menu for when the game is over
    print("It's")
    while user is not 5 and user < 1 and user > 5:
        try:
            print(Fore.LIGHTCYAN_EX, "What do you want to do now?")
            print(Fore.LIGHTCYAN_EX, '1 - Replay')
            print(Fore.LIGHTCYAN_EX, '2 - Change Category')
            print(Fore.LIGHTCYAN_EX, '3 - Custom Difficulty')
            print(Fore.LIGHTGREEN_EX, '4 - Back to Main Menu')
            print(Fore.LIGHTGREEN_EX, '5 - Quit')
            user = int(input(" Your input:"))

            if user >= 1 and user <= 5:
                break
            else:
                print(Fore.LIGHTRED_EX, 'Invalid Input!')

        except:
            print(Fore.LIGHTRED_EX, 'Invalid Input!')

    return user

class MainMenu:
    init()
    print(Fore.LIGHTCYAN_EX, 'Welcome to Hangman\n')
    user = 0
    dif = 0
    cat = 0

    while user is not 4:
        print(Fore.LIGHTYELLOW_EX, '\nMain Menu - enter a number to select game mode')
        print(Fore.LIGHTYELLOW_EX, '1 - Normal Game')
        print(Fore.LIGHTYELLOW_EX, '2 - Special Game')
        print(Fore.LIGHTYELLOW_EX, '3 - Custom Word')
        print(Fore.LIGHTGREEN_EX, '4 - Quit')
        userT = input(" Your input:")

        if check_input(userT):
            userT = userT.strip()  # Bypasses spaces
            user = int(userT[0])
        else:
            print(Fore.LIGHTRED_EX, 'Input Error! Please, try again!\n')

        if user == 1:
            user = 0  # User resets to zero.
            os.system('cls' if os.name == 'nt' else 'clear')
            print(Fore.LIGHTCYAN_EX, "\nYou chose Normal Mode!")
            over = 0
            n = NormalMode()
            word, dif, cat = getWords(dif, cat)
            n.play_game(word)
            print("aaa")
            while int(over) is not 4:
                over = overMenu(over)
                if over == 1:
                    n.play_game(getWords(dif, cat))
                if over == 2:
                    n.play_game(getWords(dif, 0))
                if over == 3:
                    n.play_game(getWords(0, 0))
                if over == 4:
                    print("\n>>>Back to Main Menu\n")
                if over == 5:
                    print(Fore.LIGHTMAGENTA_EX, '\nOK! See you next time!')
                    sys.exit()



        if user == 2:
            user = 0  # User resets to zero.
            print(Fore.LIGHTCYAN_EX, "\nYou chose Special Mode!")
            print(Fore.LIGHTCYAN_EX, "Under construction!")

        if user == 3:
            user = 0  # User resets to zero.
            print(Fore.LIGHTCYAN_EX, "\nYou chose Custom Word!")
            print(Fore.LIGHTCYAN_EX, "\nThis is a two-player game! Input a word and let someone else guess it.")

            c = CustomWord()
            c.play_game()

    print(Fore.LIGHTMAGENTA_EX, '\nOK! See you next time! o/')




if __name__ == '__main__':
    MainMenu()
