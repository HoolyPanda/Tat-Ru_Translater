# from xlrd import open_workbook
import sys
import translater
import client
import os
# from os import path

s = translater.Translater()

def MainMenu():
    # print()
    # print(os.getlogin())
    if len(sys.argv) == 2:
        # os.path.exists()
        a = os.getlogin()
        if os.path.exists('/home/' + a + '/' +  sys.argv[1]):
            path = '/home/' + os.getlogin() + '/' + sys.argv[1] 
            textFile = open(('/home/' + os.getlogin() + '/' +  sys.argv[1]), 'r').read()
            # print(textFile)
            s.Translate(lang='Ru', text=textFile)
            pass

    else:
        procText = input("Введите текст на Русском: ")
        s.Translate(lang='Ru', text=procText)
    command = input("Продолжить?(д/н): ")
    if command == "д":
        MainMenu()
    elif command == "синх":
        command = input('загр/скач?: ')
        if command == "загр":
            client.Client().PushDict()
        elif command == "скач":
            client.Client().PullDict()
        pass
    else:
        exit()

MainMenu()