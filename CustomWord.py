import getpass
from colorama import Fore

class CustomWord(object):
    def playGame(self):
        word, hint = enterWord()
        print(Fore.LIGHTYELLOW_EX, "The game is about to start!\n\n")

        #GAMELOOP
        print("The hint is " + hint)


def enterWord():
    # a and b are used to confirm the word
    a = ""
    b = " "
    while(a is not b):
        print(Fore.LIGHTMAGENTA_EX,"\n Insert the word you want.")
        a = getpass.getpass(" Don't worry, it's hidden!")
        print("*" * len(a))
        b = getpass.getpass(" Reinsert the word to make sure the spelling is correct:")
        print("*" * len(b))
        if (a == b):
            break
        print(Fore.LIGHTRED_EX,"The words don't match! Try again! ")

    print("Great! Now enter a hint: ")
    h = getpass.getpass("It can be blank if you want...\n")
    print("Sucess!")
    return a, h