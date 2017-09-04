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


class MainMenu:
    init()
    print(Fore.LIGHTCYAN_EX, 'Welcome to Hangman\n')
    user = 0

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

            try:
                n = NormalMode()
                n.play_game(getWords())
            except:  # catch every exception
                e = sys.exc_info()[0]
                print(Fore.LIGHTRED_EX, "Error : %s" % e)
                print("Check if the json files are in the root with the proper name!")

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
