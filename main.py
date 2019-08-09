# from xlrd import open_workbook
import translater
import client

s = translater.Translater()

def MainMenu():
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