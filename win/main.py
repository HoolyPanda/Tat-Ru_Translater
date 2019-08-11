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
    a = os.getlogin()
    if len(sys.argv) == 2:
        # os.path.exists()
        if os.path.exists(sys.argv[1]):
            # path = 'C:\\Users\\' + a + '\\' +  sys.argv[1] 
            pass

    else:
        procText = input("Введите текст на Русском или путь к файлу: ")
        if not os.path.exists(procText):
            s.Translate(lang='Ru', text=procText)
        else:
            textFile = open(procText, 'r',encoding='cp1251').read()
            s.Translate(lang='Ru', text=textFile)

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
        pass
try:
    MainMenu()
except Exception as e:
    print(e)
    input('')
    a = open('log', 'w+')
    a.write("log\n"+ e)
    a.close()
# input("---")