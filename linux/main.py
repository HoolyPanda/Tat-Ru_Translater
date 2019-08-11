# from xlrd import open_workbook
import sys
import translater
import client
import os
import platform
# from os import path

s = translater.Translater()

def MainMenu():
    # print()
    print(platform.system())
    if len(sys.argv) == 2:
        # os.path.exists()
        a = os.getlogin()
        if platform.system() == 'Linux':
            print(os.path.abspath(sys.argv[1])) 
            pass
        if os.path.exists('/home/' + a + '/' +  sys.argv[1]):
            textFile = open((os.path.abspath(sys.argv[1]), 'r')).read()
            s.Translate(lang='Ru', text=textFile)
            textFile.close()
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