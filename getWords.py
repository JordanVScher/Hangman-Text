#reads the json file and chooses a word
#also responsible for difficulty and category
from colorama import *
import json
import random
import sys

def getWords(dif = 0, cat = 0):
    if dif is 0:
        dif = askDifficulty()
    if cat is 0:
        cat = askCategory()

    return openFile(dif, cat)


def openFile(dif, cat):
    try:
        file = "normalWords.json" # if difficulty equals 1
        if dif == 2:
            file = "hardWords.json"

        mode = "cinema" # if category equals 1
        if cat == 2:
            mode = "literature"

        with open(file + "") as data_file:
            jsondata = json.load(data_file)

        for i in jsondata[mode]:
            print(i['word'])
            #  print(data)

        a = random.choice(jsondata[mode])
        print("O random é:" + a['word'])
        return a, dif, cat

    except:  # catch every exception
        e = sys.exc_info()[0]
        print(Fore.LIGHTRED_EX, "Error : %s" % e)
        print("Check if the json files are in the root with the proper name!")




def askCategory(): # asks for category
    cat = 0
    choice = False
    while not choice:
        try:
            print(Fore.LIGHTCYAN_EX, "Choose your category:")
            cat = input("1 - Cinema\n2 - Literature\n-->")
            if int(cat) == 1 or int(cat) == 2:
                choice = True
                print("OK!\n")
            else:
                print(Fore.LIGHTRED_EX, "Invalid input!")
        except:
            print(Fore.LIGHTRED_EX, "Invalid input!")

    return int(cat)


def askDifficulty(): # asks for difficulty
    dif = 0
    choice = False
    while not choice:
        try:
            print(Fore.LIGHTCYAN_EX, "Choose your difficulty level:")
            dif = input("1 - Normal\n2 - Hard\n-->")
            if int(dif) == 1 or int(dif) == 2:
                choice = True
                print("OK!\n")
            else:
                print(Fore.LIGHTRED_EX, "Invalid input!")
        except:
            print(Fore.LIGHTRED_EX, "Invalid input!")

    return int(dif)


